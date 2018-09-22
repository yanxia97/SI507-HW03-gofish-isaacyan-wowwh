import cards



def ask(hand1,hand2,deck):
    rank=int(input("Please choose a card rank you would like to ask the other player if they have (between 1-13):"))
    replace_card=[]
    fish = False
    for card in hand2.cards:
        if card.rank_num == rank:
            fish = True
            replace_card.append(card)
    for card in replace_card:
        hand1.add_card(hand2.remove_card(card))

    print("Player asked for " + str(rank))


    if fish ==True:
        print ("The other player had "+ str(rank))
    else:
        hand1.draw(deck)
        print ("The player had to go fish!")

def check(hand):
    card_list={}
    for card in hand.hands:
        if card.rank not in card_list.keys():
            card_list[card.rank]=1
        else:
            card_list[card.rank]+=1
    for each_rank in card_list.keys():
        if card_list[each_rank] == 4:
            print ("The player get a book of "+ str(each_rank))
            # hand.book.append(each_rank)
            # hand.cards.remove(...)
        

  # edited by wowwh
  #  Hand should add :  self.books=[]     
        

