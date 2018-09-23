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
    print("You have a hand with cards")
    for card in hand1.cards:
        print(card)
    print("The enemy:")
    for card in hand2.cards:
        print(card)
    rank=int(input("Please choose a card rank you would like to ask the other player if they have (between 1-13): "))	
    replace_card=[]    
    fish = False
    for card in hand2.cards:
        if card.rank_num == rank:
            fish = True
            replace_card.append(card)
    for card in replace_card:
        hand1.add_card(hand2.remove_card(card))

    print("Player asked for " + str(rank))

    if len(deck.cards)>0:
        if fish == True:
            print("The other player had "+ str(rank))
            print("Please continue to choose card!")
            ask(hand1,hand2,deck)
        else:
            hand1.draw(deck)
            print ("The player had to go fish!")
            if hand1.cards[-1].rank_num == rank:
                print("Please continue to choose card!")
                ask(hand1,hand2,deck)
            else:
                print("Next turn!")
    else:
        print("The deck is empty")
        if fish == True:
            print("The other player had "+ str(rank))
            print("Please continue to choose card!")
            ask(hand1,hand2,deck)






# check whether someone has 4 cards with the same rank
# param: hand of a player
# return: a list of the books (a list with rank numbers or a null list)
# edited by wowwh, commented by isaacyan
def check(hand):
    book=[]
    card_list={}
    for card in hand.cards:
        if card.rank_num not in card_list.keys():
            card_list[card.rank_num]=1
        else:
            card_list[card.rank_num]+=1
    for each_rank in card_list.keys():
        if card_list[each_rank] == 4:
            print ("The player get a book of "+ str(each_rank))
            for i in range(4):
                hand.remove_card(cards.Card(i,each_rank))
            book.append(each_rank)
    return book





# iterate for each turn until all the books are shown and jufge who wins the game.
# param: hands of the players and the remaing cards in the deck
# return:  nothing
# edited by isaacyan
def play(hand1, hand2, deck):
    turn = 0 # show whose turn is
    book1 = []
    book2 = []
    while True:
        book1 += check(hand1)
        book2 += check(hand2)        
        if len(book1)+len(book2)==13:
            if len(book1)>len(book2):
                print("Player1 wins!")
            else:
                print("Player2 wins!")
            break
        if turn%2==0:
            print("Player1's turn!")
            ask(hand1, hand2, deck)           
        else:
            print("Player2's turn!")
            ask(hand2, hand1, deck)
        turn += 1      


if __name__ == "__main__":
    deck = cards.Deck()
    deck.shuffle()
    hands= deck.deal(2,7) # deal the cards to the two players
    hand1=hands[0]
    hand2=hands[1]
    play(hand1, hand2, deck) # the player with hand 1 goes first
    # edited by isaacyan
    # adjusted by wowwh
