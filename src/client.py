import socket
import select
import errno
import sys
import threading

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234
my_username = input("Username: ")


def console(username, lock):
    while True:
        # Wait for user to input a message
        with lock:
            message = input(f'')
            # print ("\033[A                             \033[A")

            # If message is not empty - send it
            if message:
                # Encode message to bytes, prepare header and convert to bytes, like for username above, then send
                message = message.encode('utf-8')
                message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
                client_socket.send(message_header + message)
            




# Create a socket
# socket.AF_INET - address family, IPv4, some otehr possible are AF_INET6, AF_BLUETOOTH, AF_UNIX
# socket.SOCK_STREAM - TCP, conection-based, socket.SOCK_DGRAM - UDP, connectionless, datagrams, socket.SOCK_RAW - raw IP packets
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to a given ip and port
client_socket.connect((IP, PORT))

# Set connection to non-blocking state, so .recv() call won;t block, just return some exception we'll handle
client_socket.setblocking(False)

# Prepare username and header and send them
# We need to encode username to bytes, then count number of bytes and prepare header of fixed size, that we encode to bytes as well
username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)

stdout_lock = threading.Lock()
send = threading.Thread(target=console, args=(my_username, stdout_lock))
send.start()

while True:
    try:
        # Now we want to loop over received messages (there might be more than one) and print them
        while True:

            # Receive our "header" containing username length, it's size is defined and constant
            username_header = client_socket.recv(HEADER_LENGTH)

            # If we received no data, server gracefully closed a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
            if not len(username_header):
                print('Connection closed by the server')
                sys.exit()

            # Convert header to int value
            username_length = int(username_header.decode('utf-8').strip())

            # Receive and decode username
            username = client_socket.recv(username_length).decode('utf-8')

            # Now do the same for message (as we received username, we received whole message, there's no need to check if it has any length)
            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')

            # Print message
            print(f'{username} > {message}')

    except IOError as e:
        # This is normal on non blocking connections - when there are no incoming data error is going to be raised
        # Some operating systems will indicate that using AGAIN, and some using WOULDBLOCK error code
        # We are going to check for both - if one of them - that's expected, means no incoming data, continue as normal
        # If we got different error code - something happened
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error: {}'.format(str(e)))
            sys.exit()

        # We just did not receive anything
        continue

    except Exception as e:
        # Any other exception - something happened, exit
        print('Reading error: '.format(str(e)))
        sys.exit()






# import socket
# import select
# import errno
# import sys
# import re

# HEADER_LENGTH = 10
# MAX_LINE = 256
# MAX_RECIEVE_LINE = 1024

# IP = "127.0.0.1"
# PORT = 1234

# my_username = input("Username: ")
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.connect((IP, PORT))

# client_socket.setblocking(False)

# username = my_username.encode('utf-8')
# username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')

# client_socket.send(username_header + username)

# while True:
#     message = input(f'{my_username} > ')

#     if message:
#         # Encode message to bytes, prepare header and convert to bytes, like for username above, then send
#         message = message.encode('utf-8')
#         message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')

#         client_socket.send(message_header + message)

#         while True:
#             try:
#                 username_header = client_socket.recv(HEADER_LENGTH)
#                 # If we received no data, server gracefully closed a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
#                 if not len(username_header):
#                     print('Connection closed by the server')
#                     sys.exit()
#             except:
#                 pass

#             break


#         try:
#         # Now we want to loop over received messages (there might be more than one) and print them
#             while True:

#                 # Receive our "header" containing username length, it's size is defined and constant
#                 username_header = client_socket.recv(HEADER_LENGTH)

#                 # If we received no data, server gracefully closed a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
#                 if not len(username_header):
#                     print('Connection closed by the server')
#                     sys.exit()

#                 # Convert header to int value
#                 username_length = int(username_header.decode('utf-8').strip())

#                 # Receive and decode username
#                 username = client_socket.recv(username_length).decode('utf-8')

#                 # Now do the same for message (as we received username, we received whole message, there's no need to check if it has any length)
#                 message_header = client_socket.recv(HEADER_LENGTH)
#                 message_length = int(message_header.decode('utf-8').strip())
#                 message = client_socket.recv(message_length).decode('utf-8')

#                 # Print message
#                 print(f'{username} > {message}')

#         except IOError as e:
#             if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
#                 print('Reading error: {}'.format(str(e)))
#                 sys.exit()
#             continue

#         except Exception as e:
#             # Any other exception - something happened, exit
#             print('Reading error: '.format(str(e)))
#             sys.exit()

# if len(sys.argv) > 1:
#     userInput = sys.argv[1]

#     [address, portAndFile] = userInput.split(":", 1)
#     [port, fileName] = portAndFile.split('/', 1)
#     name = address
#     port = int(port)

#     regex = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
#     result = regex.match(address)

#     if not result:
#         address = socket.gethostbyname(address)

#     if not (port and fileName and address):
#         print("Entrada invalida")

# else:
#     print('usage: simplex-talk host \n', file=sys.stderr)
#     exit(1)

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     if not s:
#         print('simplex-talk: socket', file=sys.stderr)

#     if not s.connect((address, port)):
#         print('simplex-talk: connect', file=sys.stderr)
#     print('connected')

#     message = "GET /{fileName} HTTP/1.1\nHost: {address}\n".format(
#         fileName=fileName, address=name)
#     s.send(str.encode(message))

#     with open(fileName, 'wb') as f:
#         print('file opened')
#         data = bytes()
#         print('receiving data...')
#         while True:
#             dataRecieved = s.recv(MAX_RECIEVE_LINE)
#             if not dataRecieved:
#                 break
#             data += dataRecieved

#         # print("Recieved Data: ", data)
#         # write data to a file
#         header = data.split(b'\n\n')[0]
#         # print("header: ", header.decode())

#         code = header.split(b' ')[1]
#         if code.decode() == "200":
#             fileData = (data.split(header + b'\n\n'))[1]
#             f.write(fileData)
#         elif code.decode() == "400":
#             print("File not found")

#         f.close()
#         print('file close()')
#     s.close()
