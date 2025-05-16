def value(x):  # sourcery skip: assign-if-exp, remove-unnecessary-cast, switch
	x=x[:-1]
	if x == "J":
		return int(10)
	elif x == "Q":
		return int(10)
	elif x == "K": 
		return int(10)
	else:
		return(x)
		
pv= input()
dv=input()

if value(pv) == "A" and value(dv) == "A":
	print(2,"or", 12)
elif value(pv) == 'A':
	if 11+int(value(dv)) == 21 :
		print("Blackjack!")
	else:
		print(1+ int(value(dv)),"or", 11+int(value(dv)))
elif value(dv) == "A":
	if 11+int(value(pv)) == 21 :
		print("Blackjack!")
	else:
		print(1+ int(value(pv)),"or", 11+int(value(pv)))
else:
	print( int(value(pv)) + int(value(dv)))
	

