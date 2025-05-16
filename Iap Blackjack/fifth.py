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

def dealerCheck(dealerTotal, num_As):
    if dealerTotal > 16 and num_As > 0:
        num_As -= 1
        dealerTotal -= 10
    return dealerTotal, num_As

def dealerScore(card, dealerTotal, num_As):
    if card[:-1] == "K" or card[:-1] == "Q" or card[:-1] == "J":
        dealerTotal += 10
        dealerTotal, num_As = dealerCheck(total, num_As)
    elif card[:-1] == "A":
        if dealerTotal + 11 > 16:
            if dealerTotal + 1 > 16 and num_As > 0:
                dealerTotal -= 9
                num_As -= 1
            else:
                dealerTotal += 1
        else:
            dealerTotal += 11
            num_As += 1
    else:
        dealerTotal += int(card[:-1])
        dealerTotal, num_As = dealerCheck(total, num_As)
    return dealerTotal, num_As

card = input()
total = 0
num_As = 0
i = 0

while (card != "end"):
    total, num_As = score(card, total, num_As)
    i += 1
    card = input()

card = input()
dealerTotal = 0
num_As = 0
j = 0

while (card != "end"):
    dealerTotal, num_As = score(card, dealerTotal, num_As)
    j += 1
    card = input()

if (total == 21 and i == 2):
    print("Player wins!")
elif (total > 21):
    print("Dealer wins!")
elif (dealerTotal == 21 and j == 2):
    print("Dealer wins!")
elif (dealerTotal > 21):
    print("Player wins!")
elif dealerTotal > total:
    print("Dealer wins!")
elif total > dealerTotal:
    print("Player wins!")
else:
    print("Push!")
    
#=========================================================================
#Question 4

# if total == 21 and i == 2:
#     print("Blackjack!")
# elif total <= 21:
#     if num_As > 0 and total - 10 <= 21:
#         print(total - 10, "or", total)
#     else:
#         print(total)
# elif total > 21:
#     print("Bust!")
