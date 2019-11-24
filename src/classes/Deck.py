from Card import Card, CardState, Number, Suit
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
    
    @classmethod
    def shuffle(cls):
        rd.shuffle(cls.stack)
    
    @classmethod
    def reset_deck(cls):
        for suit in cls.cards:
            for card in suit:
                card.state = CardState.STACK
                if card.player != None:
                    card.player.hand = []
                cls.stack.append(card)
    
    @classmethod
    def clear_table(cls):
        for suit in cls.cards:
            for card in suit:
                if card.state == CardState.TABLE:
                    cls.stack.append(card)
                    card.state = CardState.STACK