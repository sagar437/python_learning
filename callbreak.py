import random
suits = ('heart','diamond','spade','club')
ranks = ('two','three','four','five','six','seven','eight','nine','ten','joker','king','queen','ace')	

class card():
	def __init__(self,rank,suit):
		self.rank = rank
		self.suit = suit
	def __str__(self):
		return self.rank + 'of' + self.suit

class deck():
	def __init__(self):
		self.deck = []
		for suit in suits:
			for rank in ranks:
				self.deck.append(card(rank,suit))
	def __str__(self):
        	deck_comp = ''  # start with an empty string
        	for card in self.deck:
            		deck_comp += '\n '+card.__str__() # add each Card object's print string
        	return 'The deck has:' + deck_comp
	
	def shuffle(self):
		random.shuffle(self.deck)
	
	def deal(self):
		single_card = self.deck.pop()
		return single_card
test_deck = deck()
print(test_deck)

