HEADER_LENGTH = 10


class Message():
    def __init__(self, to_others_input, reply_input):

        self.header_to_others = f"{len(to_others_input):<{HEADER_LENGTH}}".encode(
            'utf-8')
        self.header_reply = f"{(len(reply_input)):<{HEADER_LENGTH}}".encode(
            'utf-8')
        self.to_others = to_others_input.encode('utf-8')
        self.reply = reply_input.encode('utf-8')