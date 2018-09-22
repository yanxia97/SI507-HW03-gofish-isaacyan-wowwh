import cards

# SI 507 Fall 2018
# Homework 3 Extra Credit 1 - Code

# COMMENT YOUR CODE WITH:
# Section Day/Time: 004,9/19/2018,17:30-19:00
# People you worked with: wowwh

# ask for the player's with hand1 input of rank number(1-13) and check whether the other one has cards with the same rank.
# param: hands of the players and the remaing cards in the deck and who is playing
# return: nothing
# edited by wowwh, commented by isaacyan
def ask(hand1,hand2,deck):
	pass

# check whether someone has 4 cards with the same rank
# param: hand of a player
# return: a list of the books (a list with a rank number of a null list)
# edited by wowwh, commented by isaacyan
def check(hand):
	pass

# iterate for each turn until all the books are shown and jufge who wins the game.
# param: hands of the players and the remaing cards in the deck
# return:  nothing
# edited by isaacyan
def play(hand1, hand2, deck):
	turn = 0 # show whose turn is
	book1 = []
	book2 = []
	while True:
		if turn/2==0:
			fish = ask(hand1, hand2)
			book1 += check(hand1)
		else:
			fish = ask(hand2, hand1)
			book2 += check(hand2)
		turn += 1
		if len(book1)+len(book2)==13:
			if len(book1)>len(book2):
				print("Player1 wins!")
			else:
				print("Player2 wins!")
			break


if __name__ == "__main__":
	deck = cards.Deck()
	deck.shuffle()
	hand1, hand2 = deck.deal(2,7) # deal the cards to the two players
	play(hand1, hand2, deck) # the player with hand 1 goes first
	# edited by isaacyan

