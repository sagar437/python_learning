import random
def dice():
	player1_number = random.randint(1,6)
	print("player1 got the number" + str(player1_number))
	computer_number = random.randint(1,6)
	print("computer got the number" + str(computer_number))
	if player1_number > computer_number:
		print("player1 won")
	elif player1_number < computer_number:
		print("computer won")
	else:
		print("it's a draw")
while True:	
	print("do you want to start a game? Yes or no")
	answer = input()
	if answer == 'yes':
		dice()
	else:
		break
