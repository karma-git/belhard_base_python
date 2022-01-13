from itertools import product
from random import shuffle
from ah_blackjack.Picture import CardFromDeck, CardPrinter
from ah_blackjack.const import SUITS, RANKS
import colorama as clr


class Card:
    # Object properties
    def __init__(self, suit, rank, points, picture):
        self.suit = suit
        self.rank = rank
        self.points = points
        self.picture = picture

    # return message for Object instance:
    #                                   card picture and value
    def __repr__(self):
        message = self.picture + '\nPoints: ' + str(self.points)
        return message


class Deck:
    # Generate a deck of cards
    def __init__(self):
        self.cards = self._generate_deck()
        shuffle(self.cards)  # shuffle a deck

    def _generate_deck(self):
        cards = []
        for suit, rank in product(SUITS, RANKS):  # generate suits for all cards
            if rank == 'Ace':  # 11 points for ace
                points = 11
            elif rank.isdigit():  # int(card_value) if not picture
                points = int(rank)
            else:  # else picture -> 10
                points = 10
            card_instance = CardFromDeck(suit, rank)
            picture = CardPrinter.ascii_version_of_card(card_instance)
            c = Card(suit=suit, rank=rank, points=points, picture=picture)  # создается инстанс карты
            cards.append(c)
        return cards

    # take a card from the deck
    def get_card(self):
        return self.cards.pop()

    # checked how much cards left in deck
    def __len__(self):
        return len(self.cards)
