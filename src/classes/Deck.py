from Card import Card, CardState, Number, Suit
from Message import Message
import random as rd

class Deck():
    @classmethod
    def __init__(cls):
        cls.cards = {
            Suit.DIAMONDS: [Card(num, Suit.DIAMONDS) for num in Number],
            Suit.SPADES: [Card(num, Suit.SPADES) for num in Number],
            Suit.HEARTS: [Card(num, Suit.HEARTS) for num in Number],
            Suit.CLUBS: [Card(num, Suit.CLUBS) for num in Number]
        }
        cls.stack = []
        for suit in cls.cards:
            for card in suit:
                cls.stack.append(card)
        cls.table = []
    
    #/shuffle
    @classmethod
    def shuffle(cls):
        rd.shuffle(cls.stack)
        return Message("The deck was shuffled.", "The deck was shuffled.")

    #/table
    @classmethod
    def repr_table(cls):
        if len(cls.table) > 0:
            string = "Mesa: {\n "
            for card_index in range(len(cls.table)-1, -1, -1):
                string += ( "%d: %s\n" % (card_index, str(cls.table[card_index])) )
            string += "\n}"
            return Message(string, string)
        else:
            return Message("No cards on the table.", "No cards on the table.")
    
    #/reset
    @classmethod
    def reset_deck(cls):
        for suit in cls.cards:
            for card in suit:
                card.state = CardState.STACK
                if card.player != None:
                    card.player.hand = []
                cls.stack.append(card)
        return Message("The stack was reset.", "The stack was reset.")
    
    #/clear_table
    @classmethod
    def clear_table(cls):
        while len(cls.table) > 0:
            card = cls.table.pop()
            cls.stack.insert(0, card)
        return Message("All cards on the table were returned to the bottom of the stack.", "All cards on the table were returned to the bottom of the stack.")
