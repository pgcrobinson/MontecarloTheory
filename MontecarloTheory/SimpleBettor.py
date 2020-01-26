from RouletteWheel import rollDice

def simple_bettor(funds,initial_wager,wager_count):
    value = funds
    wager = initial_wager

    currentWager = 0

    while currentWager < wager_count:
        if rollDice():
            value += wager
        else:
            value -= wager

        currentWager += 1
    
    if value < 0:
        value = 'Broke'
    elif value < 10000:
        value ='Loss'
    print('Funds:', value)


x = 0 
while x <100:
    simple_bettor(10000,100,10000)
    x+=1

