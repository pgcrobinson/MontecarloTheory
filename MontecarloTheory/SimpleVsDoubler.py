from RouletteWheel import rollDice
import random
import matplotlib
import matplotlib.pyplot as plt
import time


sampleSize = 1000
startingFunds = 100
wagerSize = 10
wagerCount = 100


def doubler_bettor(funds,initial_wager,wager_count,color):
    global broke_count
    value = funds
    wager = initial_wager
    wX = []
    vY = []
    currentWager = 1
    previousWager = 'win'
    previousWagerAmount = initial_wager

    while currentWager <= wager_count:
        if previousWager == 'win':
            if rollDice():
                value += wager
                wX.append(currentWager)
                vY.append(value)
            else:
                value -= wager 
                previousWager = 'loss'
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value < 0:
                    broke_count +=1
                    break
        elif previousWager == 'loss':
            if rollDice():
                wager = previousWagerAmount * 2
                if (value - wager) < 0:
                    wager = value
                value += wager
                wager = initial_wager
                previousWager = 'win'
                wX.append(currentWager)
                vY.append(value)
            else:
                wager = previousWagerAmount * 2
                if (value - wager) < 0:
                    wager = value
                value -= wager
                previousWager = 'loss'
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value < 0:
                    broke_count +=1
                    break

        currentWager += 1
    # this guy goes cyan #
    plt.plot(wX,vY,color)

#####                                           color#
def simple_bettor(funds,initial_wager,wager_count,color):
    ####
    global broke_count
    value = funds
    wager = initial_wager
    wX = []
    vY = []
    currentWager = 1
    while currentWager <= wager_count:
        if rollDice():
            value += wager
            wX.append(currentWager)
            vY.append(value)
        else:
            value -= wager
            wX.append(currentWager)
            vY.append(value)

            ###add me
            if value < 0:
                broke_count +=1
                break
        currentWager += 1

    # this guy goes green #
    plt.plot(wX,vY,color)

    
x = 0
broke_count = 0
while x < sampleSize:             
    simple_bettor(startingFunds,wagerSize,wagerCount,'k')
    #simple_bettor(startingFunds,wagerSize*2,wagerCount,'c')
    doubler_bettor(startingFunds,wagerSize,wagerCount,'c')
    x+=1

#print(('death rate:',(broke_count/float(x)) * 100))
#print(('survival rate:',100 - ((broke_count/float(x)) * 100)))
plt.axhline(0, color = 'r')
plt.ylabel('Account Value')
plt.xlabel('Wager Count')
plt.show()