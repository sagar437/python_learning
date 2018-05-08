#!/usr/bin/python
import random
#def define_cards( ):
ranks = '2 3 4 5 6 7 8 9 10 Jack Queen King Ace'.split()
suits = 'club diamond heart spade'.split()
cards = [ ]
for suit in range(4):
	for rank in range(13):
		card_string = ranks[rank] + " of " + suits[suit]
		cards.append(card_string)
random.shuffle(cards)
x = 0
j = 13
while j <= 52:
	for i in range(1,5):
		print ("player" + str(i)) 
		y = cards[x:j]
		print(y)
		x = x + 13
		j = j + 13
		
