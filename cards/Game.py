import Player
from Deck import Deck
import random

from const import MESSAGES


class Game:
    max_pl_count = 4

    def __init__(self):
        self.players = []
        self.player = None
        self.player_pos = None
        self.all_players_count = 1
        self.deck = Deck()

    @staticmethod
    def _ask_starting(message):
        while True:
            choice = input(message)
            if choice == 'n':
                return False
            elif choice == 'y':
                return True

    def _launching(self):

        while True:
            your_name = input('Hello, write your name ') # todo: const
            if your_name:
                # Player.Player.name = your_name
                break

        # while True:
        #     bots_count = int(input('Hello, write bots count ')) #todo: const
        #     if bots_count <= self.max_pl_count - 1:  # self # Game #__name__
        #         break

        # for _ in range(bots_count):
        #     b = Player.Bot()
        #     self.players.append(b)
        #
        #     print(b, 'is created')

        self.player = Player.Player()
        self.player.name = your_name
        self.player_pos = random.randint(0, len(self.players))
        print(f'{self.player} position is: ', self.player_pos)  # it needs to be deleted
        self.players.insert(self.player_pos, self.player)

    def first_desc(self):
        for player in self.players:
            for _ in range(2):
                card = self.deck.get_card()
                player.take_card(card)

        card = self.deck.get_card()

        #tmp
        for player in self.players:
            player.print_cards()

    def start_game(self):
        message = MESSAGES.get('ask_start')  # берем сообщение из констант
        if not self._ask_starting(message=message):  # если метод вернул фолс дропаем
            exit(1)

        # generating data for starting
        self._launching()
        self.first_desc()