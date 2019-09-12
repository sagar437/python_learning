#!/usr/bin/python
def create_board(board):
	print(board[7] + ' | ' + board[8] + ' | ' + board[9])
	print(board[4] + ' | ' + board[5] + ' | ' + board[6])
	print(board[1] + ' | ' + board[2] + ' | ' + board[3])

#test_board = ['_'] * 10
#create_board(test_board)

def player_input():
	marker = ''
	while marker != 'X' or marker != 'O':
		market = input("Enter a valid input 'X' or 'O'").upper()
	if marker == 'X':
		return ('X', 'O')
	else:
		return('O', 'X')
#player_input()
	
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
		while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10] or not space_check(board, position):
			position = int(input('Chose your next position:(1-9)')
	return position

def replay():
	return input(' Do you want to play again? yes or not:').lower.startswith(y)

	
	
