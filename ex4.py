import random

xartia = []
xartiaP1=[]
xartiaP2=[]
figures = ["J", "Q", "K"]
xarti = [i for i in range(1, 11)] + figures
xartiP1= [i for i in range (11, 11)] + figures
xartiP2=[i for i in range(1, 10)]
color = ["H", "S", "C", "D"]

# O P1 xekinaei panta me tuxaia fulla
# O P2 xekinaei panta me tuxaia fulla 
sumW1=0
sumW2=0
sumDr=0
rp=0
while rp<100:
    rp+=1
    #print(rp)
    for i in xarti:
        for j in color:
            xartia.append([i,j])
    random.shuffle(xartia)
    #print("P1 joins the game")
    player1=[]
    sum1=0
    while sum1<16:
        sum1=0
        player1.append(xartia.pop())
        #print (player1)
        for card in player1:
            if card[0] in figures:
                sum1=sum1+10
            else:
                sum1=sum1+card[0]
        #print(sum1)
    #if sum1>21:
        #print("P2 wins!")
    #else:
    if sum1<=21:
        #print("P2 joins the game") #let me add one more player
        player2=[]
        sum2=0
        while sum2<16:
            sum2=0
            player2.append(xartia.pop())
            #print (player2)
            for card in player2:
                if card[0] in figures:
                    sum2=sum2+10
                else:
                    sum2=sum2+card[0]
            #print(sum2)
        if sum2>21:
            sum2=0
        if sum1>sum2:
            #print("P1 wins!")
            sumW1+=1
        #elif sum2>sum1:
            #print("P2 wins!")
        else:
            sumDr+=1
            #print("draw!") 
print("Apotelesmata gia 100 gurous") #apotelesmata xwris piragma            
sumW2=100-sumW1-sumDr
print("WINS P1: %d" %sumW1)
print("WINS P2: %d" %sumW2)
print("DRAW: %d" %sumDr)

print("--------------")

# O P1 xekinaei panta me 10 h figoura 
# O P2 den xekinaei pote me 10 h figoura 
sumW1=0
sumW2=0
sumDr=0
rp=0
while rp<100:
    rp+=1
    for i in xarti:
        for j in color:
            xartia.append([i,j])
    random.shuffle(xartia)
    for i in xartiP1:
        for j in color:
            xartiaP1.append([i,j])
    random.shuffle(xartiaP1)
    for i in xartiP2:
        for j in color:
            xartiaP2.append([i,j])
    random.shuffle(xartiaP2)
    #print("P1 joins the game")
    player1=[]
    sum1=0
    firstCardP1=0
    while sum1<16:
        sum1=0
        if firstCardP1==0:
            player1.append(xartiaP1.pop())
            firstCardP1=1
        else:
            player1.append(xartia.pop())
        #print (player1)
        for card in player1:
            if card[0] in figures:
                sum1=sum1+10
            else:
                sum1=sum1+card[0]
        #print(sum1)
    #if sum1>21:
        #print("P2 wins!")
    #else:
    if sum1<=21:
        #print("P2 joins the game") #let me add one more player
        player2=[]
        sum2=0
        firstCardP2=0
        while sum2<16:
            sum2=0
            if firstCardP2==0:
                player2.append(xartiaP2.pop())
                firstCardP2=1
            else:
                player2.append(xartia.pop())
            #print (player2)
            for card in player2:
                if card[0] in figures:
                    sum2=sum2+10
                else:
                    sum2=sum2+card[0]
            #print(sum2)
        if sum2>21:
            sum2=0
        if sum1>sum2:
            #print("P1 wins!")
            sumW1+=1
        #elif sum2>sum1:
            #print("P2 wins!")
        else:
            sumDr+=1
            #print("draw!")
print("Apotelesmata me ta piragmena filla gia 100 gurous") #apotelesmata meta to piragma 
sumW2=100-sumW1-sumDr
print("WINS P1: %d" %sumW1)
print("WINS P2: %d" %sumW2)
print("DRAW: %d" %sumDr)
