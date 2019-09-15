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
	cards = deck()
	random.shuffle(cards)
	for card in range(2):
		player_cards = cards
	
deal()	
	
		
	

###play the game###deal or stay###

####check for winner###card count more than 21###


