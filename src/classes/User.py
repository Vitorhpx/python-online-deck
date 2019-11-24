from Deck import Deck
from Message import Message
import random as rd


class User():
    def __init__(self, header, username):
        self.header = header
        self.name = username
        self.hand = []

    #/hand
    def hand_repr(self):
        if len(self.hand) > 0:
            string = "{\n "
            for card_index in range(len(self.hand)):
                string += ("%d: %s\n" %
                           (card_index, str(self.hand[card_index])))
            string += "\n}"
            return Message(string, string)
        else:
            return Message("", "You have no cards.")

    #/draw {n}
    def draw_card(self, n=1):
        string = "You draw: {\n"
        for i in range(n):
            card = Deck.stack[-1].pop(-1)
            self.hand.append(card)
            card.player = self.name
            string += str(card) + "\n"
        string += "}"
        return Message("", string)

    #/show {n}
    def show_card(self, card_index):
        string = "%s shows a %s." % (self.name, self.hand[card_index])
        return (string, string)

    #/play {index}
    def play_card(self, card_index):
        self.hand[card_index].play()
        card = self.hand[card_index].pop()
        Deck.table.append(card)
        string = "%s plays a %s.\n" % (self.name, str(card))
        return Message(string, string)

    #/play all
    def play_all(self):
        string = ""
        for card_index in range(len(self.hand)):
            single_play_message = self.play_card(card_index).to_others
            string += single_play_message
        return Message(string, string)
    
    #/roll
    def roll(self, end=10):
        result = rd.randint(1, end)
        string = "%s rolls a %d." % (self.name, result)
        return Message(string, string)
