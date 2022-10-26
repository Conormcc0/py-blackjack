import random
from card import Card
import constants


class Deck:

    def __init__(self):
        self.cards = []
        for suit in constants.suits:
            for rank in constants.ranks:
                self.cards.append(Card(suit, rank))

    # def __str__(self):
    #     for card in self.cards:
    #         print(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()
