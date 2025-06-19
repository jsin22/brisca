import random        

cards = []  
p1 = 0
p2 = 0 

def points(rank):
    if rank == 1:
        return 11
    elif rank == 3:
        return 10
    elif rank == 10:
        return 2
    elif rank == 11:
        return 3
    elif rank == 12:
        return 4
    else:
        return 0
    
def playRound(first, second, trump):
    
    trumpSuit = trump[1]
    
    p1 = first.playCard()
    p2 = second.playCard()
    
    print(p1)
    print(p2)
    
    p1Suit = p1[1]
    p2Suit = p2[1]
    
    p1Rank = p1[0]
    p2Rank = p2[0]
    
    winner = 0
    
    if p1Suit == p2Suit:
        if p1Rank > p2Rank:
            first.points += points(p1Rank)
            first.points += points(p2Rank)
            winner = 1
        else:
            second.points += points(p2Rank)
            second.points += points(p1Rank)
            winner = 2
        
    elif p2Suit == trumpSuit:
        second.points += points(p2Rank)
        second.points += points(p1Rank)
        winner = 2
   
    else:
         first.points += points(p1Rank)
         first.points += points(p2Rank)
         winner = 1   
           
    if winner == 1:
        first.lastWin = True
        second.lastWin = False
        print(first.name + " won hand: ", first.points)
    else:
        second.lastWin = True
        first.lastWin = False
        print(second.name + " won hand: ", second.points)
    
def getCard():
    
    r = random.randint(0, 39) 
    while r in cards:
        r = random.randint(0, 39)
        
    cards.append(r)
    
    suit = int(r/10)
    rank = int(r%10)
    
    rank+=1
    if rank == 8:
        rank = 11
        
    if rank == 9:
        rank = 12
        
    return (rank, suit)
       

class player():
    def __init__(self, name):
        self.cards = []
        self.points = 0
        self.name = name
        self.lastWin = False
        
    def printHand(self):
        i = 0
        for c in self.cards:
            print(i, " - ",c)
            i+=1
            
    def dealCard(self, c):
        self.cards.append(c) 
    
    def playCard(self):
        self.printHand()
        i = input (self.name + " Play Card: ")
        c = self.cards[int(i)]
        self.cards.remove(c)
        return c
        
             
def main():
    
    p1 = player("P1")
    p1.lastWin = True
    p2 = player("P2")
    
    for i in range(3):
        card = getCard()
        p1.dealCard(card)
        card = getCard()
        p2.dealCard(card)
    
    trump = getCard()
    
   
    while len(cards) < 40:
        print("\nTRUMP ------>: ", trump)
        if p1.lastWin:
            playRound(p1, p2, trump)
        else:
            playRound(p2, p1, trump) 
   
        card = getCard()
        p1.dealCard(card)
        card = getCard()
        p2.dealCard(card)

    if p1.points > p2.points:
        print("Winning Player: ", p1.name)  
    else:
        print("Winning Player: ", p2.name)               
        
if __name__ == '__main__':
    main()
