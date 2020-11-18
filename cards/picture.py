import colorama as clr


class CardFromDeck(object):
    card_values = {
        'Ace': 11,  # value of the ace is high until it needs to be low
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'Jack': 2,
        'Queen': 3,
        'King': 4
    }

    def __init__(self, suit, rank):
        """
        :param suit: The face of the card, e.g. Spade or Diamond
        :param rank: The value of the card, e.g 3 or King
        """
        self.suit = suit.capitalize()
        self.rank = rank
        self.points = self.card_values[rank]


class CardPrinter:
    @staticmethod
    def ascii_version_of_card(*cards, return_string=True):
        """
        Instead of a boring text version of the card we render an ASCII image of the card.
        :param cards: One or more card objects
        :param return_string: By default we return the string version of the card, but the dealer hide the 1st card and we
        keep it as a list so that the dealer can add a hidden card in front of the list
        """
        # we will use this to prints the appropriate icons for each card
        suits_name = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
        suits_symbols = ['♠',
                         clr.Fore.RED + '♦' + clr.Fore.LIGHTBLACK_EX,
                         clr.Fore.RED + '♥' + clr.Fore.LIGHTBLACK_EX,
                         '♣']

        # create an empty list of list, each sublist is a line
        lines = [[] for i in range(9)]

        for index, card in enumerate(cards):
            # "King" should be "K" and "10" should still be "10"
            if card.rank == '10':  # ten is the only one who's rank is 2 char long
                rank = card.rank
                space = ''  # if we write "10" on the card that line will be 1 char to long
            else:
                rank = card.rank[0]  # some have a rank of 'King' this changes that to a simple 'K' ("King" doesn't fit)
                space = ' '  # no "10", we use a blank space to will the void
            # get the cards suit in two steps
            suit = suits_name.index(card.suit)
            suit = suits_symbols[suit]

            # add the individual card on a line by line basis
            lines[0].append(clr.Fore.LIGHTBLACK_EX + clr.Back.WHITE + '┌─────────┐' + clr.Style.RESET_ALL)
            lines[1].append(clr.Fore.LIGHTBLACK_EX + clr.Back.WHITE + '│{}{}       │'.format(rank,
                                                                                             space) + clr.Style.RESET_ALL)  # use two {} one for char, one for space or char
            lines[2].append(clr.Fore.LIGHTBLACK_EX + clr.Back.WHITE + '│         │' + clr.Style.RESET_ALL)
            lines[3].append(clr.Fore.LIGHTBLACK_EX + clr.Back.WHITE + '│         │' + clr.Style.RESET_ALL)
            lines[4].append(clr.Fore.LIGHTBLACK_EX + clr.Back.WHITE + '│    {}    │'.format(suit) + clr.Style.RESET_ALL)
            lines[5].append(clr.Fore.LIGHTBLACK_EX + clr.Back.WHITE + '│         │' + clr.Style.RESET_ALL)
            lines[6].append(clr.Fore.LIGHTBLACK_EX + clr.Back.WHITE + '│         │' + clr.Style.RESET_ALL)
            lines[7].append(
                clr.Fore.LIGHTBLACK_EX + clr.Back.WHITE + '│       {}{}│'.format(space, rank) + clr.Style.RESET_ALL)
            lines[8].append(clr.Fore.LIGHTBLACK_EX + clr.Back.WHITE + '└─────────┘' + clr.Style.RESET_ALL)

        result = []
        for index, line in enumerate(lines):
            result.append(''.join(lines[index]))

        # hidden cards do not use string
        if return_string:
            return '\n'.join(result)
        else:
            return result

    @staticmethod
    def ascii_version_of_hidden_card(*cards):
        """
        Essentially the dealers method of print ascii cards. This method hides the first card, shows it flipped over
        :param cards: A list of card objects, the first will be hidden
        :return: A string, the nice ascii version of cards
        """
        # a flipper over card. # This is a list of lists instead of a list of string becuase appending to a list is better then adding a string
        lines = [['┌─────────┐'],
                 ['│░░░░░░░░░│'],
                 ['│░░░░░░░░░│'],
                 ['│░░░░░░░░░│'],
                 ['│░░░░░░░░░│'],
                 ['│░░░░░░░░░│'],
                 ['│░░░░░░░░░│'],
                 ['│░░░░░░░░░│'],
                 ['└─────────┘']]

        # store the non-flipped over card after the one that is flipped over
        cards_except_first = CardPrinter.ascii_version_of_card(*cards[1:], return_string=False)
        for index, line in enumerate(cards_except_first):
            lines[index].append(line)

        # make each line into a single list
        for index, line in enumerate(lines):
            lines[index] = ''.join(line)

        # convert the list into a single string
        return '\n'.join(lines)
