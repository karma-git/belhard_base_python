from names import get_first_name
import colorama as clr


colorama_colors = {
    'BLACK' : clr.Fore.BLACK,
    'RED' : clr.Fore.BLACK,
    'GREEN' : clr.Fore.GREEN,
    'YELLOW' : clr.Fore.YELLOW,
    'BLUE' : clr.Fore.BLUE,
    'MAGENTA' : clr.Fore.MAGENTA,
    'CYAN' : clr.Fore.CYAN,
    'WHITE' : clr.Fore.WHITE,
# LIGHTBLACK_EX
# LIGHTRED_EX
# LIGHTGREEN_EX
# LIGHTYELLOW_EX
# LIGHTBLUE_EX
# LIGHTMAGENTA_EX
# LIGHTCYAN_EX
# LIGHTWHITE_EX
}


def colored(color, text):
    """
    take color and text and return colored text
    """
    global colorama_colors
    colored_text = colorama_colors.get(color.upper()) + str(text) + clr.Style.RESET_ALL
    return colored_text


SUITS = ['Diamonds', 'Clubs', 'Spades', 'Hearts']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
PRINTED = {rank: f'***{rank}***' for rank in RANKS}

MESSAGES = {
    'ask_start': 'Want to play?(y/n) ',
    'ask_card' : 'Want new card?(y/n) ',
    'dealer_fall': 'Dealer has just fallen! All players in game are win',
    'eq': '{player} player has {points} points so it equal with dealer points\n {player} bid will be back',
    'win': '{} player are win',
    'lose': '{} player are lose',
    'rerun': 'Want to play again?(y/n)',
    'alive_players' : colored('CYAN', '\nPlayers in the game:\n'),
    'first_desk' : colored('yellow', '\n!!! First shuffle !!!\n'),
    'circle_num': colored('green', '\n!!! {} shuffle !!!\n'),
    'dealer_game': colored('magenta', '\nStart Game versus Dealer !!! \n'),
}


def random_name():
    return get_first_name(gender="male")


NAMES = [random_name() for _ in range(20)]
