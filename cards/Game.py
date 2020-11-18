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
        self.players_enough = []

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
            your_name = input('Hello, write your name: ')  # todo: const
            if your_name:
                # Player.Player.name = your_name
                break

        while True:
            bots_count = int(input('Hello, write bots count: '))  # todo: const
            if bots_count <= self.max_pl_count - 1:  # self # Game #__name__
                break

        for _ in range(bots_count):
            b = Player.Bot()
            self.players.append(b)

            print(b, 'is created')  # is it neaded?

        self.player = Player.Player()
        self.player.name = your_name
        self.player_pos = random.randint(0, len(self.players))
        print(f'{self.player} position is: ', self.player_pos)  # it needs to be deleted
        self.players.insert(self.player_pos, self.player)

    def first_desc(self):
        """
        First desk, all players will take 2 cards
        """
        # take first 2 cards for each player
        for player in self.players:
            for _ in range(2):
                card = self.deck.get_card()
                player.take_card(card)
        # cards print
        for player in self.players:
            player.print_cards()

    def is_next_desk_needed(self):
        enough = []  # votes of the players
        for player in self.players:
            enough.append(player.enough) # send player decision to vote
        # True if at least one player need a card
        if False in enough:
            self.circle_count += 1
            return True
        # False otherwise
        else:
            return False

    # Game Service methods
    def check_fall(self, player):
        if player.full_points > 21:
            return True
        else:
            return False

    def remove_player(self, player):
        # player.print_cards() # I wont print card of a player when he just fall
        if isinstance(player, Player.Player):
            print(f'{self.player} fall!')
        elif isinstance(player, Player.Bot):
            print(player, 'are fall')
        self.players.remove(player)

    def ask_card(self):
        # new circle print
        print(MESSAGES.get('circle_num').format(self.circle_count))
        for player in self.players:
            if player.ask_card():
                card = self.deck.get_card()
                player.take_card(card)

                # Ace 1 point mechanic
                if card.rank == 'Ace' and player.full_points > 21:
                    player.full_points -= 10

            elif not player.ask_card():
                player.enough = True
            player.print_cards()
            sleep(2)

            if self.check_fall(player):
                self.remove_player(player)

        # is_stop = self.check_stop(player)

    # main Game method
    def start_game(self):
        message = MESSAGES.get('ask_start')  # берем сообщение из констант
        if not self._ask_starting(message=message):  # если метод вернул фолс дропаем
            exit(1)

        # generating data for starting
        self._launching()

        self.first_desc()  # first desk

        while self.is_next_desk_needed():
            self.ask_card()
        else:
            print("Vizhivshie")
            for player in self.players:
                player.print_cards()