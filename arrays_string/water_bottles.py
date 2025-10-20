numBottles = 10
numExchange = 3

def drink(numBottles,numExchange):
    emptyBottles = 0
    ex = 0
    drank = 0
    while((numBottles != 0) or emptyBottles>=numExchange):
        if(emptyBottles < numExchange and numBottles != 0):
            drank+=numBottles
            emptyBottles += numBottles
            numBottles = 0
            print(f"drank {drank} bottles")
        else:
            while(emptyBottles>=numExchange):
                emptyBottles -= numExchange
                numExchange+=1
                ex +=1 
                numBottles += 1
                print(f"Exchange {ex} times")
    print(f"Total bottles drank = {drank}")
drink(numBottles,numExchange)