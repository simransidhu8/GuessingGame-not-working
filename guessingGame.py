import random
randomNumber = random.randint(0, 10)
chances = 5
guess = input("Guess a number between 1-9: ")
while chances < 5 :
    if guess == randomNumber :
        print("YOU WON!!!")
        break
    if not chances < 0 : 
        print("YOU LOSE!!! The number is", randomNumber)