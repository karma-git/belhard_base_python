import Player
from Deck import Deck
import random
from time import sleep

from const import MESSAGES


class Game:
    max_pl_count = 4
    circle_count = 1

    def __init__(self):
        self.players = []
        self.player = None
        self.player_pos = None
        self.all_players_count = 1
        self.deck = Deck()
        self.want_circle = [True]

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
            your_name = input('Hello, write your name ')  # todo: const
            if your_name:
                # Player.Player.name = your_name
                break

        while True:
            bots_count = int(input('Hello, write bots count '))  # todo: const
            if bots_count <= self.max_pl_count - 1:  # self # Game #__name__
                break

        for _ in range(bots_count):
            b = Player.Bot()
            self.players.append(b)

            print(b, 'is created')

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

        # tmp
        for player in self.players:
            player.print_cards()

    def stand(self):
        for player in self.players:
            if not player.ask_card():
                player.stand = None
            else:
                player.stand = True

    def remove_player(self, player):
        player.print_cards()
        if isinstance(player, Player.Player):
            print(f'{self.player} fall!')
        elif isinstance(player, Player.Bot):
            print(player, 'are fall')
        self.players.remove(player)

    def another_desc(self):
        self.circle_count += 1
        print(MESSAGES.get('circle_num').format(self.circle_count))
        self.want_circle.clear()
        for player in self.players:
            if player.stand:
                for _ in range(1):
                    card = self.deck.get_card()
                    player.take_card(card)
                    self.want_circle.append(True)
                    if player.full_points > 21:
                        self.remove_player(player)

        # tmp
        for player in self.players:
            player.print_cards()

    def check_winner(self):
        pass

    def start_game(self):
        message = MESSAGES.get('ask_start')  # берем сообщение из констант
        if not self._ask_starting(message=message):  # если метод вернул фолс дропаем
            exit(1)

        # generating data for starting
        self._launching()

        self.first_desc()
        self.stand()
        while True in self.want_circle:
            self.another_desc()
            self.stand()
            sleep(2)
        else:
            for player in self.players:
                print(f'{player} - winner!')
                player.print_cards()
