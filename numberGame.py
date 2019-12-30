import random

answer = random.randint(0,25)
guess = 0

def main(answer, guess):
    count = 0
    
    while count < 3 and answer != guess:
        guess = int(input("please enter your guess (0 to 25) : "))
        
        if guess < answer:
            print("oops..too low!")
        elif guess > answer:
            print("uh-oh..too high!")
        else:
            print("BINGOO! great guess!!")
        count += 1
    
    if count == 3 and answer!=guess:
        print("nice try..the correct number is {}. thanks for playing!".format(answer))
    
main(answer, guess)