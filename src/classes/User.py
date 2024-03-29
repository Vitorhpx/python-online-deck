from .Deck import Deck
from .Message import Message
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
                string += ("%d: %s\n" % (card_index, str(self.hand[card_index])))
            string += "}"
            return Message("", string)
        else:
            return Message("", "You have no cards.")

    #/draw {n}
    def draw_card(self, n=1):
        string = "You draw: {\n"
        for i in range(n):
            card = Deck.stack.pop(-1)
            self.hand.append(card)
            card.player = self
            string += str(card) + "\n"
        string += "}"
        return Message("%s drew %d card(s)" % (self.name, n), string)

    #/show {n}
    def show_card(self, card_index):
        string = "%s shows a %s." % (self.name, self.hand[card_index])
        return Message(string, string)

    #/play {index}
    def play_card(self, card_index):
        self.hand[card_index].play()
        card = self.hand.pop(card_index)
        Deck.table.append(card)
        string = "%s plays card #%d: %s.\n" % (self.name, card_index, str(card))
        return Message(string, string)

    #/play all
    def play_all(self):
        string = ""
        for card_index in range(len(self.hand)):
            single_play_message = self.play_card(0).to_others
            string += single_play_message.decode('utf-8')
        return Message(string, string)

    #/roll
    def roll(self, end=6):
        result = rd.randint(1, end)
        string = "%s rolls a %d." % (self.name, result)
        return Message(string, string)
