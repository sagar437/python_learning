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

def hit():
	new_card = deck.pop()
	return new_card


player_response = input("do you want to hit or stay")
if player_response == 'hit':
	pnew_card = hit()
	dnew_card = hit()
	player1_hand.append(pnew_card)
	dealer_hand.append(dnew_card)
total_player = 0
total_dealer = 0
for p_card in player1_hand:
	total_player += int(p_card)
for d_card in dealer_hand:
	total_dealer += int(d_card)
if total_player > 21 and total_dealer < 21:
	print(total_player)
	print(total_dealer)
	print("dealer win")
elif total_dealer > 21 and total_player <21:
	print(total_player)
	print(total_dealer)
	print("player win")
else:
	print(total_player)
	print(total_dealer)
	print("continue playing")
