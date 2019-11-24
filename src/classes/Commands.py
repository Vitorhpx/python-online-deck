from User import User
from Deck import Deck


def hand(user: User):
    # TODO: SEND TO USER HIS HAND
    return user.hand_repr()


def play(user: User, cardIndex):
    return user.play_card(card_index)


def shuffle(deck: Deck):
    return deck.shuffle()


def table(user: User, deck: Deck):
    # TODO: SEND TO ALL USERS THE TABLE
    return deck.table()


def cleanTable(deck: Deck):
    # TODO: SEND TO ALL USERS THE TABLE was clean
    return deck.clear_table()


def draw(user: User):
    # TODO: SEND TO his new hand
    return user.draw_card()


def show(user: User):
    # TODO: show card
    return user


def roll(user: User):
    ##TODO: roll
    return


def getCommand(commandString, user: User, deck: Deck):
    [command, parameter] = commandString.splice(' ', 1)

    if command == 'help':
        return
    elif command == 'hand':
        return hand(user)
    elif command == 'play':
        return play(user, parameter)
    elif command == 'shuffle':
        return shuffle(deck)
    elif command == 'table':
        return table(user, deck)
    elif command == 'clean-table':
        return cleanTable(deck)
    elif command == 'draw':
        return draw()
    elif command == 'show':
        return
    elif command == 'roll':
        return
    elif command == 'reset':
        return
    else:
        return null
