# Python-project-1
import random as rnd

def rollNsidedDie(N):
    number = rnd.randint(1,N)
    return number
    
num_dice = raw_input("How many dice do you want to row? ")
num_side = raw_input("How many sided dices do you want to roll? ")

for i in range(int(num_dice)):
    print "Roll " + str(i)