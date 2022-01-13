from names import get_first_name
import colorama as clr

colorama_colors = {
    'BLACK': clr.Fore.BLACK,
    'RED': clr.Fore.BLACK,
    'GREEN': clr.Fore.GREEN,
    'YELLOW': clr.Fore.YELLOW,
    'BLUE': clr.Fore.BLUE,
    'MAGENTA': clr.Fore.MAGENTA,
    'CYAN': clr.Fore.CYAN,
    'WHITE': clr.Fore.WHITE,
    'LIGHTWHITE_EX': clr.Fore.LIGHTWHITE_EX,
    'LIGHTRED_EX': clr.Fore.LIGHTRED_EX,
    'LIGHTBLUE_EX': clr.Fore.LIGHTBLUE_EX,
    'LIGHTYELLOW_EX': clr.Fore.LIGHTYELLOW_EX,
    'LIGHTMAGENTA_EX': clr.Fore.LIGHTMAGENTA_EX
}


def colored(color, text):
    """
    The method takes color and some str and return colored string.
    """
    global colorama_colors
    colored_text = colorama_colors.get(color.upper()) + str(text) + clr.Style.RESET_ALL
    return colored_text


SUITS = ['Diamonds', 'Clubs', 'Spades', 'Hearts']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

MESSAGES = {
    # Start message:

    # System messages: Yellow / Light_Yellow
    'ask_name': colored('LIGHTYELLOW_EX', """Hello Stranger, what's your name?: """),
    'ask_bot_count': colored('LIGHTYELLOW_EX', 'Choose bots count (from 0 to 3): '),
    'ask_start': colored('LIGHTYELLOW_EX', 'Wanna play ah_blackjack?(y/n): '),
    'ask_card': colored('LIGHTYELLOW_EX', 'Wanna "hit" a card?(y/n): '),
    'ask_bet': colored('LIGHTYELLOW_EX', 'Make your bet (1-19 $): '),
    'ask_rerun': colored('LIGHTYELLOW_EX', 'Wanna play next desk?(y/n)'),
    # Shuffle
    'initial_deal': colored('yellow', '\n!!! Initial deal !!!\n'),
    'next_deal': colored('yellow', '\n!!! Deal {} !!!\n'),
    'alive_players': colored('cyan', '\nRemained players:\n'),
    'no_players': colored('cyan', '\nThere are no players in game\n'),
    'falling': colored('blue', '{player} has just fallen!\n'
                                 'Lost {money}$ -> money left {bank}'),
    'player_bank': colored('yellow', """{player}'s current bank {bank}$"""),
    'no_money': colored('yellow', """Sorry, your account is empty.\nGame over."""),
    'no_money': f"""{colored('yellow', 'Sorry, your account is empty.')}\n
                    {colored('LIGHTMAGENTA_EX', 'Game Over.')}""",
    # Dealer
    'dealer_fall': colored('magenta', 'Dealer has just fallen! All remained players in the game won (bet x2)'),
    'eq': colored('magenta', """{player} hand value equal with dealer's. 
                    Bet coast has been returned to player's account. """),
    'dealer_game': colored('magenta', '\nStart Game versus Dealer !!! \n'),

    # Results
    'win': colored('GREEN', '{player} player won'
                            '\nhand value -> {score} | '
                            'profit -> {profit}$ | '
                            'bank -> {bank}$'),
    'equal': colored('LIGHTWHITE_EX', '{player} players bet has been returned'
                                      '\nhand value -> {score} | '
                                      'bet -> {profit}$ | '
                                      'bank -> {bank}$'),

    'lose': colored('RED', '{player} player lost'
                           '\nscore -> {score} | '
                           '-money -> {profit}$ | '
                           'bank -> {bank}$'),

}


def random_name():
    """
    Generating a name for bot.
    """
    return get_first_name(gender="male")


NAMES = list({random_name() for _ in range(20)})  # set due to we want to get unique names for bots
