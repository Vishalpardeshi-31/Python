import random

number=random.randint(1,100)
count=0
while(True):
    guess=int(input("Guess the number"))
    if guess>number:
        print("YOUR GUESS IS HIGHER, TRY LOWER")
    else:
        print("YOUR GUESS IS LOWER, TRY HIGHER") 
    count+=1   
    if guess==number:
        print("CONGRATS YOU GUESS THE NUMBER(YOU WON!!!)") 
        break      

print(f"You guessed {count} times ")
