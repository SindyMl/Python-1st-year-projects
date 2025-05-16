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

card = input()
total = 0
num_As = 0
i = 0

while (card != "end"):
    total, num_As = score(card, total, num_As)
    i += 1
    card = input()

if total == 21 and i == 2:
    print("Blackjack!")
elif total <= 21:
    if num_As > 0 and total - 10 <= 21:
        print(total - 10, "or", total)
    else:
        print(total)
elif total > 21:
    print("Bust!")