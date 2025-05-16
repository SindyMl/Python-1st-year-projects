def check(total, num_As):
    if total > 21 and num_As > 0:
        num_As -= 1
        total -= 10
    return total, num_As

def score(card, total, num_As):
    if card[:-1] == "K" or card[:-1] == "Q" or card[:-1] == "J":
        total += 10
        total, num_As = check(total, num_As)
    elif card[:-1] == "A":
        if total + 11 > 21:
            if total + 1 > 21 and num_As > 0:
                total -= 9
                num_As -= 1
            else:
                total += 1
        else:
            total += 11
            num_As += 1
    else:
        total += int(card[:-1])
        total, num_As = check(total, num_As)
    return total, num_As

def output_score(hand):
    total, num_As, i = 0, 0, 0

    for card in hand:
        total, num_As = score(card, total, num_As)

    if total == 21 and i == 2:
        return "Blackjack!"
    elif total <= 21:
        if num_As > 0 and total - 10 <= 21:
            return str(total - 10) + " or " + str(total)
        else:
            return str(total)
    elif total > 21:
        return "Bust!"

def is_blackjack(hand):
    if len(hand) == 2 and output_score(hand) == "Blackjack!":
        return True
    return False

def is_bust(hand):
    if output_score(hand) == "Bust!":
        return True
    return False

def usableAce(num_As):
	if num_As > 0:
		return True
	else:
		return False

def usableTable(player,dealer):
	if player == 18 and dealer<=8:
		return "Stand"
	elif player > 18 :
		return "Stand"
	else:
		return "Hit"
		
def table(player,dealer):
	if player == 12 and 4 <= dealer <=6 :
		return "Stand"
	elif player >= 13 and dealer < 7:
		return "Stand"
	elif player >= 17:
		return "Stand"
	else:
		return "Hit"

def get_advice(player_hand, dealer_hand):
    dealer, v = score(dealer_hand, 0, 0)
    player, Ace = 0, 0

    for card in player_hand:
        player, Ace = score(card, player, Ace)
        
    if usableAce(Ace):
        return usableTable(player, dealer)
    else:
        return table(player, dealer)


def get_high_score(hand):
    total = 0
    num_As = 0

    for card in hand:
        total, num_As = score(card, total, num_As)

    return total

def get_winner(player_hand, dealer_hand):
    total, num_As, i = 0, 0, 0

    for card in player_hand:
        total, num_As = score(card, total, num_As)
        i += 1

    dealerTotal, num_As, j = 0, 0, 0

    for card in dealer_hand:
        dealerTotal, num_As = score(card, dealerTotal, num_As)
        j += 1

    if (total == 21 and i == 2):
        return ("Player wins!")
    elif (total > 21):
        return ("Dealer wins!")
    elif (dealerTotal == 21 and j == 2):
        return ("Dealer wins!")
    elif (dealerTotal > 21):
        return ("Player wins!")
    elif (dealerTotal > total):
        return ("Dealer wins!")
    elif (total > dealerTotal):
        return ("Player wins!")
    else:
        return ("Push!")

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
