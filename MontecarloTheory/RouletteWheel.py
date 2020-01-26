import random

def rollDice():
    roll = random.randint(1,100)
    
    if roll == 100:
        #print (roll,'roll was 100, you lose. What are the odds?! Play again!')
        return False
    elif roll <= 50:
        #print (roll,'roll was 1-50, you lose.')
        return False
    elif 100 > roll >= 50:
        #print (roll,'roll was 51-99, you win! *pretty lights flash* (play more!)')
        return True

