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
		print("Enter a valid input")
	
		
