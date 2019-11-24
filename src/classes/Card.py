from enum import Enum

class CardState(Enum):
    STACK = 0
    HAND = 1
    TABLE = 2

class Suit(Enum):
    DIAMONDS = 0
    SPADES = 1
    HEARTS = 2
    CLUBS = 3

class Number(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8 
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

class Card():
    def __init__(self, number, suit, player=None):
        self.state = CardState.STACK if player==None else CardState.HAND
        self.player = player
        self.number = number
        self.suit = suit
    
    def play(self):
        self.state = CardState.TABLE
        self.player = None

    def __repr__(self):
        return "[ %s %s ]" % (str(self.number.name), str(self.suit.name))