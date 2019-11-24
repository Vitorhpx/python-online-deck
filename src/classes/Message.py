HEADER_LENGTH = 10

class Message():
    def __init__(self, to_others, reply):
        self.header_to_others = f"{len(to_others):<{HEADER_LENGTH}}".encode('utf-8')
        self.header_reply = f"{len(reply):<{HEADER_LENGTH}}".encode('utf-8')
        self.to_others = to_others
        self.reply = reply