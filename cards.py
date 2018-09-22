import random
import unittest

# SI 507 Fall 2018
# Homework 3 Extra Credit 1 - Code

# COMMENT YOUR CODE WITH:
# Section Day/Time: 004,9/19/2018,17:30-19:00
# People you worked with: wowwh

class Card(object):
	suit_names =  ["Diamonds","Clubs","Hearts","Spades"]
	rank_levels = [1,2,3,4,5,6,7,8,9,10,11,12,13]
	faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}

	def __init__(self, suit=0,rank=2):
		self.suit = self.suit_names[suit]
		if rank in self.faces: # self.rank handles printed representation
			self.rank = self.faces[rank]
		else:
			self.rank = rank
		self.rank_num = rank # To handle winning comparison

	def __str__(self):
		return "{} of {}".format(self.rank,self.suit)

class Deck(object):
	def __init__(self): # Don't need any input to create a deck of cards
		# This working depends on Card class existing above
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card) # appends in a sorted order

	def __str__(self):
		total = []
		for card in self.cards:
			total.append(card.__str__())
		# shows up in whatever order the cards are in
		return "\n".join(total) # returns a multi-line string listing each card

	def pop_card(self, i=-1):
		# removes and returns a card from the Deck
		# default is the last card in the Deck
		return self.cards.pop(i) # this card is no longer in the deck -- taken off

	def shuffle(self):
		random.shuffle(self.cards)

	def replace_card(self, card):
		card_strs = [] # forming an empty list
		for c in self.cards: # each card in self.cards (the initial list)
			card_strs.append(c.__str__()) # appends the string that represents that card to the empty list
		if card.__str__() not in card_strs: # if the string representing this card is not in the list already
			self.cards.append(card) # append it to the list

	def sort_cards(self):
		# Basically, remake the deck in a sorted way
		# This is assuming you cannot have more than the normal 52 cars in a deck
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card)

	# deal the deck to different hands
	# If the number of cards per hand is set to -1, all of the cards should be dealt, 
	# even if this results in an uneven number of cards per hand.
	# param: the number of hands, the number of cards per hand
	# return: a list of Hands
	def deal(self, hand_number, hand_size):
		hand_list=[]
		if hand_number==-1:
			while len(self.cards)>0:
				hand = Hand()
				for i in range(hand_size):
					hand.add_card(self.pop_card())
					if len(self.cards)==0:
						break
				hand_list.append(hand)
		else:
			for i in range(hand_number):
				hand = Hand()
				for j in range(hand_size):
					hand.add_card(self.pop_card())
				hand_list.append(hand)
		return hand_list

class Hand(object):
	# create the Hand with an initial set of cards
	# param: a list of cards
	def __init__(self, init_cards=[]):
		self.cards = []
		for card in init_cards: 
			self.cards.append(card)
					
	# add a card to the hand
	# silently fails if the card is already in the hand
	# param: the card to add
	# returns: nothing
	def add_card(self, card):
		card_strs = [] # forming an empty list
		for c in self.cards: # each card in self.cards (the initial list)
			card_strs.append(str(c)) # appends the string that represents that card to the empty list
		if str(card) not in card_strs: # if the string representing this card is not in the list already
			self.cards.append(card) # append it to the list

	# remove a card from the hand
	# param: the card to remove
	# returns: the card, or None if the card was not in the Hand
	def remove_card(self, card):
		i = 0  # indicate which card it is
		for selfcard in self.cards:
			if str(selfcard) == str(card): # judge whether the card is same as teh card to remove
				self.cards.pop(i)# remove the card
				return card # return the card
			else:
				i += 1
		return None # return None

	# draw a card from a deck and add it to the hand
	# side effect: the deck will be depleted by one card
	# param: the deck from which to draw
	# returns: nothing
	def draw(self, deck):
		self.cards.append(deck.pop_card())

	# look for pairs of cards in a hand and removes them.
	# if there are three of a kind, only two should be removed
	# param: nothing
	# return nothing
	def remove_pairs(self):
		dup_card=Hand(self.cards)
		havecards = {}
		for card in dup_card.cards:
			if havecards.__contains__(card.rank):
				self.remove_card(havecards[card.rank])
				self.remove_card(card)
				del havecards[card.rank]
			else:
				havecards[card.rank]=card
		


#############
## The following is a line to run all of the tests you include:
if __name__ == "__main__":
## verbosity 2 to see detail about the tests the code fails/passes/etc.