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
    'LIGHTBLUE_EX': clr.Fore.LIGHTBLUE_EX
    # LIGHTBLACK_EX
    # LIGHTGREEN_EX
    # LIGHTYELLOW_EX

    # LIGHTMAGENTA_EX
    # LIGHTCYAN_EX

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
    'ask_card': 'Want new card?(y/n) ',
    'ask_bet' : 'Make your bet (1-19 $): ',
    'dealer_fall': 'Dealer has just fallen! All players in game are win',
    'eq': '{player} player has {points} points so it equal with dealer points\n {player} bid will be back',

    'win': colored('LIGHTRED_EX', '{player} player is win'
                                  '\nscore -> {score} | '
                                  'profit -> {profit} | '
                                  'bank -> {bank}'),
    'equal': colored('LIGHTWHITE_EX', '{player} players bet has been returned'
                                     '\nscore -> {score} | '
                                     'bet -> {profit} | '
                                     'bank -> {bank}'),

    'lose': colored('LIGHTWHITE_EX', '{player} player is lose'
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
    return get_first_name(gender="male")


NAMES = [random_name() for _ in range(20)]
