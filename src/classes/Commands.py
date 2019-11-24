from .User import User
from .Deck import Deck
from .Message import Message

MANUAL = """
/hand\n
/shuffle\n
/draw {? number}\n
/play {index | all}\n
/table\n
/clean-table\n
/show {index}\n
/roll {? range}\n
/reset\n
/stack\n
/table-draw
"""


def getCommand(commandString, user: User):
<<<<<<< HEAD
    try:
        [command, *params] = commandString.split(' ', 1)
        if command == 'help':
            return Message("", MANUAL)
        elif command == 'hand':
            return user.hand_repr()
        elif command == 'play':
            if params[0] == 'all':
                return user.play_all()
            else:
                return user.play_card(params[0])
        elif command == 'shuffle':
            return Deck.shuffle()
        elif command == 'table':
            return Deck.repr_table()
        elif command == 'clean-table':
            return Deck.clear_table()
        elif command == 'draw':
            if len(params) == 1:
                return user.draw_card(params[0])
            else:
                return user.draw_card()
        elif command == 'show':
            return user.show_card(params[0])
        elif command == 'roll':
            if len(params) == 1:
                return user.roll(params[0])
            else:
                return user.roll()
        elif command == 'reset':
            return Deck.reset_deck()
        elif command == 'stack':
            return Deck.count_deck()
        elif command == 'table-draw':
            return Deck.draw_table()
=======
    # try:
    [command, *params] = commandString.split(' ', 1)
    if command == '/help':
        return Message("", MANUAL)
    elif command == '/hand':
        return user.hand_repr()
    elif command == '/play':
        if params[0] == 'all':
            return user.play_all()
>>>>>>> Fixes some erros
        else:
            return user.play_card(int(params[0]))
    elif command == '/shuffle':
        return Deck.shuffle()
    elif command == '/table':
        return Deck.repr_table()
    elif command == '/clean-table':
        return Deck.clear_table()
    elif command == '/draw':
        if len(params) == 1:
            return user.draw_card(int(params[0]))
        else:
            return user.draw_card()
    elif command == '/show':
        return user.show_card(int(params[0]))
    elif command == '/roll':
        if len(params) == 1:
            return user.roll(int(params[0]))
        else:
            return user.roll()
    elif command == '/reset':
        return Deck.reset_deck()
    elif command == 'stack':
        return Deck.count_deck()
    else:
        return Message("", "Invalid Command")


# except:
#     return Message("", "Invalid Command")
