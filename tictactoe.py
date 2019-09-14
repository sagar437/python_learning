#!/usr/bin/python
def create_board(board):
	print(board[7] + ' | ' + board[8] + ' | ' + board[9])
	print(board[4] + ' | ' + board[5] + ' | ' + board[6])
	print(board[1] + ' | ' + board[2] + ' | ' + board[3])

#test_board = ['_'] * 10
#create_board(test_board)

#def player_input():
#	marker = ''
#	while not (marker == 'X' or marker == 'O'):
#		marker = input("Enter a valid input 'X' or 'O'").upper()
#	if marker == 'X':
#		return ('X', 'O')
#	else:
#		return('O', 'X')
#player_input()
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
	
def place_maker(board, marker, position):
	board[position] = marker

def win_check(board,marker):
	return((board[1] == board[2] == board[3] == marker) or
	       (board[4] == board[5] == board[6] == marker) or
	       (board[7] == board[8] == board[9] == marker) or
	       (board[1] == board[5] == board[9] == marker) or
	       (board[3] == board[5] == board[7] == marker))

#place_maker(test_board, 'X', 5)
#create_board(test_board)		
import random
def chose_first():
	if random.randint(0,1) == 0:
		return 'player1'
	else:
		return 'player2'

def space_check(board, position):
	return board[position] == ' '

def full_board_check(board):
	for i in range(1,10):
		if space_check(board, i):
			return False
		else:
			return True

def player_choice(board):
	position = 0
    
    	while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        	position = int(input('Choose your next position: (1-9) '))
        
    	return position


def replay():
	return input('Do you want to play again? yes or not:').lower.startswith(y)

print("welcome to tictactoe")
	
test_board = ['_']*10
create_board(test_board)
player1_marker, player2_marker = player_input()
turn = chose_first()
print(turn + 'will go first')
play_game = input("Do you want to start the game? yes or no")
if play_game.lower()[0] == 'y':
	game_on = True
else:
	game_on = False
while game_on:
	if turn == 'player1':
		create_board(test_board)
		position = player_choice(test_board)
		place_maker(test_board, player1_marker, position)
		if win_check(test_board, player1_marker):
			create_board(test_board)
			print("Congratulations you are the winner:player1")
			game_on = False
		else:
			if full_board_check(test_board):
				create_board(test_board)
				print("the game is draw")
				game_on = False
				break
			else:
				turn = 'player2'
	else:
		create_board(test_board)
		position = player_choice(test_board)
		place_maker(test_board, player2_marker, position)
		if win_check(test_board, player2_marker):
			create_board(test_board)
			print("congratulations you are the winnder:player2")
			game_on = False
		else:
			if full_board_check(test_board):
				create_board(test_board)
				print("the game is draw")
				game_on = False
				break
			else:
				turn = 'player1'
	if not replay():
		break
