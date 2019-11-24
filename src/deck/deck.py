import random

class Deck:
  def __init__(self):
    self.cards = range(52)
    self.table = []

  def add_carts_to_bottom(newCards):
    self.cards = self.cards.concat(newCards)

  def clean_table():
    self.add_carts_to_bottom(self.table)
    self.table = []
  
  def shuffle():
    random.shuffle(self.cards)

  def getTable():
    return self.table
  
  def getDeck():
    return self.cards

