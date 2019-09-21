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

class player():
	def __init__(self,name):
		self.name = name
		self.hand = []

	def sayHello(self):
        	print("Hi! My name is" + self.name)
        	return self

		
	def draw(self,deck,num=1):
		for _ in range(num):
			card = deck.deal()
			self.hand.append(card)
		return self.hand

	def showhand(self):
		print("{} has {}".format(self.name,self.hand))
		return self

	def discard(self):
		return self.hand.pop()


mydeck = deck()
mydeck.shuffle()
#print(mydeck)
bob = player("Bob")
bob.sayHello()
bob.draw(mydeck,13)
bob.showhand()


