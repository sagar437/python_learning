import os
import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

def deal():
	hand = []
	for i in range(2):
		random.shuffle(deck)
		card = deck.pop()
		if card == 11:card == "J"
		if card == 12:card == "Q"
		if card == 13:card == "K"
		if card == 14:card == "A"
		hand.append(card)
	return hand
player1_hand = deal()
dealer_hand = deal()
print(player1_hand)
print(dealer_hand)
#print("do you want to hit or stay")
#if player_response == 'hit':
	
	
