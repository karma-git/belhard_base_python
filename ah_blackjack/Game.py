import ah_blackjack.Player as Player
from ah_blackjack.Deck import Deck
import random
from time import sleep

from ah_blackjack.const import MESSAGES, colorama_colors, colored


class Game:
    """
    Main game object.
    """
    # global variables
    max_pl_count = 4
    deal_number = 1

    def __init__(self):
        self.players = []  # list of players instance in current game
        self.player = None  # property for real player instance
        self.deck = Deck()  # deck of cards instance
        self.players_enough = []  # anchor for game with dealer
        self.dealer = Player.Dealer()  # dealer instance
        self.max_bet, self.min_bet = 20, 0  # bet limit
        self.losers = []  # container for

    @staticmethod
    def _ask_starting(message):
        """
        Game starter question.
        """
        while True:
            choice = input(message)
            if choice == 'n':
                return False
            elif choice == 'y':
                return True

    def _launching(self):
        """
        Data for launch game.
        """
        # Ask Player.Player name
        while True:
            your_name = input(MESSAGES.get('ask_name'))
            if your_name:
                break
        # Ask bots count
        while True:
            bots_count = int(input(MESSAGES.get('ask_bot_count')))
            if bots_count <= self.max_pl_count - 1:
                break
        # bot creating
        for _ in range(bots_count):
            b = Player.Bot()
            self.players.append(b)
            print(b, 'is created')
        # Player instance creating: name + player pos
        self.player = Player.Player()
        self.player.name = your_name
        self.player_pos = random.randint(0, len(self.players))
        print(f'{self.player} position is: ', self.player_pos)
        self.players.insert(0, self.player)

    def _restart(self):
        """
        Method for clear desk params & print player's bank
        """
        self.deck = Deck()  # New deck
        self.dealer = Player.Dealer()  # CLEAR dealer
        self.players_enough.clear()  # anchor for game with dealer
        self.deal_number = 1
        # move players who lose in last game to new
        while self.losers:
            self.players.append(self.losers.pop())
        # clear player cards, hands value, and ask_card
        for player in self.players:
            player.cards.clear()
            self.full_points = None
            player.enough = False
            print(MESSAGES.get('player_bank').format(player=player,
                                                     bank=player.money))

    def ask_bet(self):
        """
        Ask a player about bet
        """
        for player in self.players:
            player.change_bet(self.max_bet, self.min_bet)

    def initial_deal(self):
        """
        Initial_deal, all players will take 2 cards
        """
        print(MESSAGES.get('initial_deal'))
        for player in self.players:
            for _ in range(2):
                card = self.deck.get_card()
                player.take_card(card)
        # cards print
        for player in self.players:
            player.print_cards()

    def is_next_desk_needed(self):
        """
        Anchor which check, will remained player ready to play versus dealer.
        Main mechanic:
                    if no enough=False in players_enough
                    -> means all players in the game wont take a card
                    -> so is_next_desk_needed returns false
                    -> start game: alive players versus dealer
        """
        self.players_enough.clear()  # clear anchor for game with dealer
        for player in self.players:
            self.players_enough.append(player.enough)  # send player decision to anchor
        # Method return True if at least one player need a card (player.enough=False in players_enough)
        if False in self.players_enough:
            self.deal_number += 1
            return True
        # False otherwise
        else:
            return False

    # Game Service methods
    def check_fall(self, player):
        """
        The method check much, for a player.
        Return True if so, otherwise False.
        """
        if player.full_points > 21:
            return True
        else:
            return False

    def remove_player(self, player):
        """
        The method for deletion a player for current alive players list.
        And append him into losers container.
        Print how much money info also.
        """
        print(MESSAGES.get('falling').format(player=player,
                                             money=player.bet,
                                             bank=player.money))
        self.players.remove(player)
        self.losers.append(player)

    def ask_card(self):
        """
        The method suggest to take a card for a player.
        - Print shuffle num
            - Give a card for a player if he want it.
                + ace overflow mechanic.
                + print his hand after it.
                + check falling.
        Else:
            - Set player.enough to True
                                        * player will not take a card during this game.
                + print player hand.
        """
        # 1). Print shuffle num
        print(MESSAGES.get('next_deal').format(self.deal_number))
        for player in self.players:
            if player.ask_card():
                card = self.deck.get_card()
                player.take_card(card)
                # * Ace overflow mechanic.
                if card.rank == 'Ace' and player.full_points > 21:
                    player.full_points -= 10
                # hand print
                player.print_cards()
                # check falling
                if self.check_fall(player):
                    self.remove_player(player)
                sleep(2)
            # if wont a card
            elif not player.ask_card():
                player.enough = True
                player.print_cards()
                sleep(2)

    # Dealer methods
    def play_with_dealer(self):
        """
        Remained players play versus dealer.
        For black_jack rules, dealer continue take a card until his hand value take 17. He can't take a card after.
        """
        card = self.deck.get_card()
        self.dealer.take_card(card)
        while self.dealer.ask_card():
            card = self.deck.get_card()
            self.dealer.take_card(card)
        self.dealer.print_cards()

    def stats_printer(self, player, action, score, bet, x, bank):
        """
        Method print player statistic.
        :param player: player instance
        :param action: take most common situation after game_vs_dealer: win, lose, equal
        :param score: player hand value
        :param bet: player bet
        :param x: bet multiply
        :param bank: remained money on player account
        :return: None
        """
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
        """
        The method calculate and print result of game.
        """
        # dealer fall, all remained players won.
        if self.dealer.full_points > 21:
            print(MESSAGES.get('dealer_fall'))
            for winner in self.players:
                winner.money += winner.bet * 2
                self.stats_printer(player=winner,
                                   action='win',
                                   score=winner.full_points,
                                   bet=winner.bet,
                                   x=2,
                                   bank=winner.money)
        # if dealer not fall
        else:
            for player in self.players:
                # equal
                if player.full_points == self.dealer.full_points:
                    player.money += player.bet
                    self.stats_printer(player=player,
                                       action='equal',
                                       score=player.full_points,
                                       bet=player.bet,
                                       x=1,
                                       bank=player.money)
                # player win vs dealer
                elif player.full_points > self.dealer.full_points:
                    player.money += player.bet * 2
                    self.stats_printer(player=player,
                                       action='win',
                                       score=player.full_points,
                                       bet=player.bet,
                                       x=2,
                                       bank=player.money)
                # player lose vs dealer
                elif player.full_points < self.dealer.full_points:
                    self.stats_printer(player=player,
                                       action='lose',
                                       score=player.full_points,
                                       bet=player.bet,
                                       x=1,
                                       bank=player.money)

    def losers_stats(self):
        pass

    ### DEBUG ###
    def _debug(self):
        """
        :) debugger
        """
        for player in self.players:
            print(f'{player} -> enough? {player.enough}')

    ### main Game method ###
    def start_game(self):
        # Ask about game initialization
        message = MESSAGES.get('ask_start')
        if not self._ask_starting(message=message):
            exit(1)

        # Ask player name, creating bots, set player pos
        self._launching()

        # While Player.Player have money:
        while self.player.money > 0:

            # clear tmp data (players hands, bets, and other service info)
            self._restart()

            # ask players about their bets
            self.ask_bet()
            # first desk
            self.initial_deal()
            sleep(2.5) # small freeze

            # while at least one player want to get a card, do:
            while self.is_next_desk_needed():
                self.ask_card()

            # If no one of the remained players want a card:
            # print remained players list
            if self.players:
                print(MESSAGES.get('alive_players'))
                for player in self.players:
                    player.print_cards()

                # & Initialize Game vs Dealer
                print(MESSAGES.get('dealer_game'))
                self.play_with_dealer()
                # results of the game versus dealer
                self.check_winner()
                self.losers_stats()
            # if all players have been fall
            else:
                print(MESSAGES.get('no_players'))

            # new game asking
            if not self._ask_starting(MESSAGES.get('ask_rerun')):
                break
        # Money left
        else:
            print(MESSAGES.get('no_money'))