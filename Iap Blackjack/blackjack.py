"""
File:   blackjack.py
Author: Steve James <steven.james@wits.ac.za>
"""


"""
Complete the functions below. You may include any additional functions you like
"""


def output_score(hand):
    """
    Function that takes in a hand and returns the value(s) as a string
    """
    # TODO: complete this
    pass

def is_blackjack(hand):
    """
    Whether the hand represents a Blackjack hand. Return True if it is blackjack, False otherwise
    """
    # TODO: complete this
    pass

def is_bust(hand):
    """
    Whether the hand is bust (exceeds 21). Return True if it is bust, False otherwise
    """
    # TODO: complete this
    pass

def get_advice(player_hand, dealer_hand):
    """
    Computes a suggestion as to the action to take given the cards. Return either 'Hit' or 'Stand'
    """
    # TODO: complete this


def get_high_score(hand):
    """
     Returns the maximum (non-bust) value of the hand. If the hand contains an ace,
     this means the higher of the two values is picked, provided it does not exceed 21.
    """
    # TODO: complete this
    pass


def get_winner(player_hand, dealer_hand):
    """
    Given the player's hand and the dealer's hand, return a string signifying who won (or whether it's a push)
    """
    # TODO: complete this
    pass


"""
Do not modify any code below this comment!
"""

import random


class Deck:

    def __init__(self):
        self._cards = list()
        self._rng = random.Random(42)
        self.reset()

    def _rank_to_string(self, rank):
        special = {
            1: 'A',
            11: 'J',
            12: 'Q',
            13: 'K'
        }
        return special.get(rank, str(rank))

    def reset(self):
        self._cards.clear()
        for rank in range(1, 14):
            r = self._rank_to_string(rank)
            for suit in ['h', 'c', 's', 'd']:
                self._cards.append(r + suit)
        self._rng.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()



def get_input(message, legal_options):
    while True:
        print(message, end='')
        option = input()
        if len(option) == 0:
            continue
        option = option[0].upper()
        if option in legal_options:
            return option
        else:
            print("Invalid input '{}'".format(option))


def hand_to_string(hand):
    return '{} -> {}'.format(
        ' '.join(hand),
        output_score(hand)
    )


def play_round(deck):
    player_hand = list()
    dealer_hand = list()
    deck.reset()

    dealer_hand.append(deck.draw())
    player_hand.append(deck.draw())
    player_hand.append(deck.draw())

    print('Dealer shows {}'.format(hand_to_string(dealer_hand)))
    print('Player shows {}'.format(hand_to_string(player_hand)))
    if is_blackjack(player_hand):
        print('Player wins!')
        return

    # Player's turn
    playing = True
    while playing and not is_bust(player_hand):
        action = get_input('(H)it, (S)tand, or (A)dvice? ', {'H', 'S', 'A'})
        if action == 'H':
            player_hand.append(deck.draw())
            print('Player shows {}'.format(hand_to_string(player_hand)))
        elif action == 'S':
            playing = False
        else:
            print('Advice: {}'.format(get_advice(player_hand, dealer_hand[0])))

    if playing:
        # player must be bust
        print('Dealer wins!')
        return

    # dealer's turn
    while not is_bust(dealer_hand) and get_high_score(dealer_hand) < 17:
        dealer_hand.append(deck.draw())
        print('Dealer shows {}'.format(hand_to_string(dealer_hand)))

    print(get_winner(player_hand, dealer_hand))


if __name__ == '__main__':

    running = True
    deck = Deck()
    while running:
        option = get_input('(N)ew round or (Q)uit? ', {'N', 'Q'})
        if option == 'N':
            play_round(deck)
            print('******************************************')
        elif option == 'Q':
            running = False
