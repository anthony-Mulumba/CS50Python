#import all functions inside random in the memory
import random  

#import only the function choice inside random module in the memory
#from random import choice

cards = ["jack","queen","king"]
coin = random.choice(["tails", "Pondu"])

#Random number from 1 to 100
number = random.randint(1, 10)
#print(number)

#This function shuffle cards
random.shuffle(cards)
for card in cards:
    print(card)