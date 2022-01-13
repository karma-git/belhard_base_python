import abc
from ah_blackjack.Deck import Deck
import colorama as clr
import random
from ah_blackjack.const import MESSAGES, NAMES
from ah_blackjack.Picture import CardPrinter, CardFromDeck


class AbstractPlayer(abc.ABC):
    """
    An abstract player (Player, Bot, Dealer)
    """
    def __init__(self):
        self.cards = []  # player hand
        self.bet = 0
        self.name = None
        self.full_points = None  # players hand value
        self.money = 100
        self.enough = False  # Is the player want to get a card at the next shuffle?

    def change_points(self):
        """
        This method is designed too recalculate player hand value
        """
        self.full_points = sum([card.points for card in self.cards])

    def take_card(self, card):
        """
        This method add a card to player hand and call recalculate hand sum (via change_points method)
        """
        self.cards.append(card)
        self.change_points()

    @abc.abstractmethod
    def ask_card(self):
        """
        Is player want to get a new card?
        Abstract due to different for AI and real player.
        """
        pass

    def hand_printer(self):
        """
        The method prints a card picture.
        """
        cards_list = list()  # list, because we want to print cards in one line
        for card in self.cards:  # player hand
            card = CardFromDeck(card.suit, card.rank)  # unpack dictionary
            cards_list.append(card)  # list for print
        else:  # when for done
            hand_print = CardPrinter.ascii_version_of_card(*cards_list)  # complete ascii graphics
            print(hand_print)

    def print_cards(self):
        """
        Add Player name and value of printed hand.
        """
        print(self, "hand:")  # Player name + data
        self.hand_printer()  # hand printer
        print('Hand value: ', self.full_points, '\n')  # hand value


class Player(AbstractPlayer):
    """
    Real player
    """
    def change_bet(self, max_bet, min_bet):
        """
        Ask a player about his bet and sub its value from player money.
        """
        while True:
            value = int(input(MESSAGES.get('ask_bet')))
            if value < max_bet and value > min_bet:  # limits for bet
                self.bet = value
                self.money -= self.bet
                break
        print(f'Your bet is {self.bet}')

    def ask_card(self):
        """
        This method ask player about take card if value less then 21.
        """
        if self.full_points == 21:
            return False
        elif self.enough:
            return False
        choice = input(MESSAGES.get('ask_card'))
        if choice == 'y':
            return True
        elif choice == 'n':
            self.enough = True
            return False

    def get_name(self, name):
        """
        Set player name.
        """
        name = clr.Fore.GREEN + self.name

    def __repr__(self):
        return clr.Fore.GREEN + self.name + clr.Style.RESET_ALL  # const.colored ?


class Bot(AbstractPlayer):
    """
    AI player.
    """
    def __init__(self):
        super().__init__()  # adding additional properties
        self.max_points = random.randint(17, 20)  # set max points, where a bot stop ask cards
        self.name = random.choice(NAMES) + '_Bot'  # generate bot_name

    def change_bet(self, max_bet, min_bet):
        """
        Random bet for bot.
        """
        self.bet = random.randint(min_bet, max_bet)
        self.money -= self.bet
        print(self, 'gives: ', self.bet)

    def ask_card(self):
        """
        Bot will ask a card, if his max points less then full points
        """
        if self.full_points < self.max_points:
            return True
        else:
            return False

    def __repr__(self):
        name = self.name
        return name


class Dealer(AbstractPlayer):
    """
    Dealer object.
    """
    max_points = 17  # as in black_jack rules, Dealer wont take a card when his points 17 or higher

    def ask_card(self):
        """
        Bot will ask a card, if his max points less then 17
        """
        if self.full_points < self.max_points:
            return True
        else:
            return False

    def __repr__(self):
        self.name = 'Dealer'
        return self.name