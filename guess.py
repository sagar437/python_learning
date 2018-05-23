import random
import sys
game_input = ' '
computer_score = 0
player_score = 0
while (game_input != 'exit'):
	game_input = input("type exit to exit the game: ")
	if game_input != 'exit':
		computer_input = int(random.randint(1,9))
		print("enter the input for player: ")
		player_input = int(input())
		print("the number for computer is: " + str(computer_input))
		if player_input > computer_input:
			print("you guess too high")
			computer_score = computer_score + 1
	
			print("computer score: " + str(computer_score) + "'" + "player score: " + str(player_score))

		elif player_input < computer_input:
			print("you guess too low")
			computer_score = computer_score + 1

			print("computer score: " + str(computer_score) + "'" + "player score: " + str(player_score))
		else:
			print("you guessed it correct")
			player_score = player_score + 1
			print("computer score: " + str(computer_score) + "'" + "player score: " + str(player_score))

	else: 
		print("you typed exit")
		sys.exit()
