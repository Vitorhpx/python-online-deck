from Deck import Deck

class User():
    def __init__(self, ip_address, username):
        self.ip_address = ip_address
        self.name = username
        self.hand = []

    #/hand
    def hand_repr(self):
        if len(self.hand) > 0:
            string = "{\n "
            for card_index in range(len(self.hand)):
                string += ( "%d: %s\n" % (card_index, str(self.hand[card_index])) )
            string += "\n}"
            return string
        else:
            return "Nenhuma carta."
    
    #/draw {n}
    def draw_card(self, n=1):
        string = "You draw: {\n"
        for i in range(n):
            card = Deck.stack[-1].pop(-1)
            self.hand.append(card)
            card.player = self.ip_address
            string += str(card) + "\n"
        string += "}"
        return string
    
    #/show {n}
    def show_card(self, card_index):
        return "%s shows a %s." % (self.name, self.hand[card_index])

    #/play {index}
    def play_card(self, card_index):
        self.hand[card_index].play()
        card = self.hand[card_index].pop()
        Deck.table.append(card)
        return "%s plays a %s.\n" % (self.name, str(card))
    
    #/play all
    def play_all(self):
        for card_index in range(len(self.hand)):
            self.play_card(card_index)
        
