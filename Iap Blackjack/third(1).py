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
		
dealer, v = score(input(), 0, 0)
player=0
Ace=0
for i in range(2):
	player, Ace = score(input(),player,Ace)
	
if usableAce(Ace):
	print(usableTable(player,dealer))
else:
	print(table(player,dealer))
