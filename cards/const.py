from names import get_first_name
import colorama as clr

colorama_colors = {
    'BLACK': clr.Fore.BLACK,
    'RED': clr.Fore.BLACK,
    'GREEN': clr.Fore.GREEN,
    'YELLOW': clr.Fore.YELLOW,
    'LIGHTYELLOW_EX' : clr.Fore.LIGHTYELLOW_EX,
    'BLUE': clr.Fore.BLUE,
    'MAGENTA': clr.Fore.MAGENTA,
    'CYAN': clr.Fore.CYAN,
    'WHITE': clr.Fore.WHITE,
    'LIGHTWHITE_EX': clr.Fore.LIGHTWHITE_EX,
    'LIGHTRED_EX': clr.Fore.LIGHTRED_EX,
    'LIGHTBLUE_EX': clr.Fore.LIGHTBLUE_EX
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
    'ask_start': 'Want to play?(y/n) ',
    'ask_card': 'Want a new card?(y/n) ',
    'ask_bet': 'Make your bet (1-19 $): ',
    'dealer_fall': 'Dealer has just fallen! All remained players in the game won (bet x2)',
    'eq': """{player} hand score equal with dealer's. Bet has been returned to player's account. """,

    'win': colored('GREEN', '{player} player is win'
                                  '\nscore -> {score} | '
                                  'profit -> {profit} | '
                                  'bank -> {bank}'),
    'equal': colored('LIGHTWHITE_EX', '{player} players bet has been returned'
                                      '\nscore -> {score} | '
                                      'bet -> {profit} | '
                                      'bank -> {bank}'),

    'lose': colored('RED', '{player} player is lose'
                                     '\nscore -> {score} | '
                                     '-money -> {profit} | '
                                     'bank -> {bank}'),

    'rerun': 'Want to play again?(y/n)',
    'alive_players': colored('CYAN', '\nPlayers in the game:\n'),
    'first_desk': colored('yellow', '\n!!! First shuffle !!!\n'),
    'circle_num': colored('green', '\n!!! {} shuffle !!!\n'),
    'dealer_game': colored('magenta', '\nStart Game versus Dealer !!! \n'),
    'no_players': colored('CYAN', '\nThere are no players in game\n')
    }


def random_name():
    """
    Generating a name for bot.
    """
    return get_first_name(gender="male")


NAMES = list({random_name() for _ in range(20)})  # set due to we want to get unique names for bots
