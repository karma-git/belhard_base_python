from itertools import product
from random import shuffle
from picture import CardFromDeck, CardPrinter
from const import SUITS, RANKS, PRINTED
import colorama as clr


class Card:
    # конструктор, у карты есть масть, карта, ее валуе и картинка
    def __init__(self, suit, rank, points, picture):
        self.suit = suit
        self.rank = rank
        self.points = points
        self.picture = picture

    # репр объекта карты, ранк, масть, валуе
    def __repr__(self):
        message = self.picture + '\nPoints: ' + str(self.points)
        return message


class Deck:
    # генерируется колода
    def __init__(self):
        self.cards = self._generate_deck()
        shuffle(self.cards)  # картуется

    def _generate_deck(self):
        cards = []
        for suit, rank in product(SUITS, RANKS):  # вместо генератора итертулс
            if rank == 'Ace':  # если туз то его валуе = 11
                points = 11
            elif rank.isdigit():  # если без картинки то int от ранка
                points = int(rank)
            else:  # инча карта с картинкой и 10-ка
                points = 10
            # picture = PRINTED.get(rank)  # из констант забирается картинка по ключу ранк
            card_instance = CardFromDeck(suit, rank)
            picture = CardPrinter.ascii_version_of_card(card_instance)
            c = Card(suit=suit, rank=rank, points=points, picture=picture)  # создается инстанс карты
            cards.append(c)  # объект аппендится в лист и колоджа попадает в Deck.cards
        return cards

    # позволяет доставать карту из колоды и возвращает ее
    def get_card(self):
        return self.cards.pop()

    # позволяет смотреть длину колоды (достали ли из нее карту)
    def __len__(self):
        return len(self.cards)
