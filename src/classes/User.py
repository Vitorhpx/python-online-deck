from Deck import Deck

class User():
    def __init__(self, ip_address, username):
        self.ip_address = ip_address
        self.name = username
        self.hand = []

    def hand_repr(self):
        if len(self.hand) > 0:
            string = "{\n "
            for card_index in range(len(self.hand)):
                string += ( "%d: %s\n" % (card_index, str(self.hand[card_index])) )
            string += "\n}"
            return string
        else:
            return "Nenhuma carta."
    
    def draw_card(self):
        card = Deck.stack[-1].pop(-1)
        self.hand.append(card)
        card.player = self.ip_address

    def play_card(self, card_index):
        self.hand[card_index].play()
        card = self.hand[card_index].pop()
        Deck.table.append(card)
        return "%s plays a %s.\n" % (self.name, str(card))