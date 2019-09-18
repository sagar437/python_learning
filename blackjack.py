###define card deck####
import random
def deck():
	cards = []
	rank_cards = '2 3 4 5 6 7 8 9 10 Joker Queen king Ace'.split()
	face_cards = 'spade heart diamond club'.split()
	for rank_card in range(13):
		for face_card in range(4):
			card_string = rank_cards[rank_card] + "of" + face_cards[face_card]
			cards.append(card_string)
	return cards  

#print(deck())

###deal the card####2 cards each randomly###
def deal():
	test_cards = deck()
#	print(test_cards)
	player_cards = []
	dealer_cards = []
#	random.shuffle(test_cards)
	while len(player_cards) < 2:
		random.shuffle(test_cards)
		for card in test_cards:
			print(card)
			player_cards.append(card)
#			test_cards.remove(card)
#	for card in test_cards:
#		random.shuffle(test_cards)
#		while len(dealer_cards) < 2:
#			dealer_cards.append(card)
	print(player_cards)
#	print(dealer_cards)
deal()

	
deal()	
	
		
	

###play the game###deal or stay###

####check for winner###card count more than 21###


