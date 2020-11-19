import Player
from Deck import Deck
import random
from time import sleep

from const import MESSAGES, colorama_colors, colored


class Game:
    """
    Main game object.
    """
    # global variables
    max_pl_count = 4
    circle_count = 1

    def __init__(self):
        self.players = []  # list of players instance in current game
        self.player = None  # property for real player instance
        self.all_players_count = 1  # TODO is it needed?
        self.deck = Deck()
        self.players_enough = []
        self.dealer = Player.Dealer()
        self.max_bet, self.min_bet = 20, 0
        self.losers = []

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
            bots_count = int(input('Hello, write bots count (3 max): '))  # todo: const
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
        self.players.insert(0, self.player)

    def _restart(self):
        self.deck = Deck() # New dec
        self.dealer = Player.Dealer() # CLEAR dealer
        self.players_enough.clear() # restart
        self.circle_count = 1

        while self.losers:
            self.players.append(self.losers.pop())

        for player in self.players:
            player.cards.clear()
            self.full_points = None
            player.enough = False

    def ask_bet(self):
        for player in self.players:
            player.change_bet(self.max_bet, self.min_bet)

    def first_desc(self):
        """
        First desk, all players will take 2 cards
        """
        # take first 2 cards for each player
        print(MESSAGES.get('first_desk'))
        for player in self.players:
            for _ in range(2):
                card = self.deck.get_card()
                player.take_card(card)
        # cards print
        for player in self.players:
            player.print_cards()

    def is_next_desk_needed(self):
        self.players_enough.clear()  # votes of the players
        for player in self.players:
            self.players_enough.append(player.enough)  # send player decision to vote
        # True if at least one player need a card
        if False in self.players_enough:
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
        # if isinstance(player, Player.Player):
        #     print(f'{self.player} fall!')
        # elif isinstance(player, Player.Bot):
        print(player, ' has just fallen!\n')
        self.players.remove(player)
        self.losers.append(player)

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
                # hand print
                player.print_cards()
                if self.check_fall(player):
                    self.remove_player(player)
                sleep(2)
            # if wont a card
            elif not player.ask_card():
                player.enough = True
            player.print_cards()
            sleep(2)



        # is_stop = self.check_stop(player)

    # Dealer methods
    def play_with_dealer(self):
        card = self.deck.get_card()  #
        self.dealer.take_card(card)  # first card
        while self.dealer.ask_card():
            card = self.deck.get_card()
            self.dealer.take_card(card)
        self.dealer.print_cards()

    def stats_printer(self, player, action, score, bet, x, bank):
        # print(f"{player} is win -> "
        #       f"score {colored('yellow', player.full_points)} ->"
        #       f"profit {colored('yellow', player.bet * x)} ( all bank ->{player.money}) ")
        if action == 'win':
            print(MESSAGES.get('win').format(player=player,
                                             score=score,
                                             profit=bet * x,
                                             bank=bank))
        elif action == 'equal':
            print(MESSAGES.get('equal').format(player=player,
                                               score=score,
                                               profit=bet * x,
                                               bank=bank))
        elif action == 'lose':
            print(MESSAGES.get('lose').format(player=player,
                                             score=score,
                                             profit=bet,
                                             bank=bank))

    def check_winner(self):
        if self.dealer.full_points > 21:
            # all win
            print(MESSAGES.get('dealer_fall'))

            for winner in self.players:
                winner.money += winner.bet * 2
                self.stats_printer(player=winner,
                                   action='win',
                                   score=winner.full_points,
                                   bet=winner.bet,
                                   x=2,
                                   bank=winner.money)

        else:
            for player in self.players:
                if player.full_points == self.dealer.full_points:
                    player.money += player.bet
                    # print(MESSAGES.get('eq').format(player=player,
                    #                                    points=player.full_points))
                    # self.stats_printer(player, 1)
                    self.stats_printer(player=player,
                                       action='equal',
                                       score=player.full_points,
                                       bet=player.bet,
                                       x=1,
                                       bank=player.money)

                elif player.full_points > self.dealer.full_points:
                    player.money += player.bet * 2
                    self.stats_printer(player=player,
                                       action='win',
                                       score=player.full_points,
                                       bet=player.bet,
                                       x=2,
                                       bank=player.money)

                elif player.full_points < self.dealer.full_points:
                    # print(MESSAGES.get('lose').format(player))
                    # print(f"{player} is lose -> "
                    #       f"score {colored('blue', player.full_points)} ->"
                    #       f"profit {colored('blue', player.bet)} ( all bank ->{player.money}) ")
                    self.stats_printer(player=player,
                                       action='lose',
                                       score=player.full_points,
                                       bet=player.bet,
                                       x=1,
                                       bank=player.money)

    # DEBUG
    def _debug(self):
        for player in self.players:
            print(f'{player} -> enough? {player.enough}')

    # main Game method
    def start_game(self):
        message = MESSAGES.get('ask_start')  # берем сообщение из констант
        if not self._ask_starting(message=message):  # если метод вернул фолс дропаем
            exit(1)

        # generating data for starting
        self._launching()

        while self.player.money > 0:
            self._restart()
            self.ask_bet()

            self.first_desc()  # first desk
            sleep(2.5)

            self._debug()

            # Player versus dealer
            while self.is_next_desk_needed():
                self._debug()
                self.ask_card()
            # else:
            #     for player in self.players:
            #         player.print_cards()

            # Game vs Dealer
            if self.players != []:
                print(MESSAGES.get('alive_players'))

                for player in self.players:
                    player.print_cards()

                print(MESSAGES.get('dealer_game'))
                self.play_with_dealer()
                self.check_winner()
            else:
                print(MESSAGES.get('no_players'))


            # new
            if not self._ask_starting(MESSAGES.get('rerun')):
                break
