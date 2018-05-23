#!/usr/bin/python
import random
import sys
player_input = ' '
while  (player_input != 'no' ):
	print("Do you want to play a new game?")
	player_input = input("yes or no: ")
	if player_input == 'yes':
	
		options = [ 'rock', 'paper', 'scissors' ]
		player1_input = input("please enter rock,paper or scissors for player1: ")
		player2_input = random.choice(options)
		print("computer entered: " + player2_input)

		def compare(x,y):
			if (x == 'rock'  and y == 'scissors'):
				print("Player1 is the winner")
			elif (y == 'rock'  and x == 'scissors'):
                		print("Player2 is the winner")
			elif (x == 'paper'  and y == 'scissors'):
				print("Player2 is the winner")
			elif (y == 'paper'  and x == 'scissors'):
                		print("Player1 is the winner")
			elif (x == 'paper' and y == 'rock'):
				print("player1 is the winner")
			elif ( x == y ):
				print("Draw")
			elif (y == 'paper' and x == 'rock'):
                		print("player2 is the winner")
			else:
				print("not a valid input")

		compare(player1_input,player2_input)
	else:
		print("exit out of game")
		sys.exit()

