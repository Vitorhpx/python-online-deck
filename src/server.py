import socket as socket
import select as select
import threading as threading
from classes.User import User

HEADER_LENGHT = 10
HOST = '10.0.0.191'
PORT = 1234
MAX_PENDING = 10
MAX_LINE = 256
MAX_SEND_LINE = 1024


def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGHT)
        if not len(message_header):
            return False
        message_length = int(message_header.decode('utf-8').strip())
        return {
            'header': message_header,
            "data": client_socket.recv(message_length)
        }
    except:
        return False


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(MAX_PENDING)
    sockets_list = [s]
    clients = {}
    while True:
        read_sockets, _, exception_sockets = select.select(
            sockets_list, [], sockets_list)
        for notified_socket in read_sockets:
            if notified_socket == s:
                client_socket, client_address = s.accept()
                user_message = receive_message(client_socket)
                if user_message is False:
                    continue
                userHeader = user_message['header'].decode('utf-8')
                userName = user_message['data'].decode('utf-8')
                sockets_list.append(client_socket)
                clients[client_socket] = User(userHeader, userName)
                print(
                    'Accepted new connection from {}:{}, username: {}'.format(
                        *client_address, userName))
            else:
                message = receive_message(notified_socket)
                if message is False:
                    print('Closed connection from: {}'.format(user.name))
                    sockets_list.remove(notified_socket)
                    del clients[notified_socket]
                    continue
                user = clients[notified_socket]
                print(
                    f'Received message from {user.name}: {message["data"].decode("utf-8")}'
                )
                for client_socket in clients:
                    if client_socket != notified_socket:

                        client_socket.send(
                            user.header.encode('utf-8') +
                            user.name.encode('utf-8') + message['header'] +
                            message['data'])

        for notified_socket in exception_sockets:
            sockets_list.remove(notified_socket)
            del clients[notified_socket]
