import random
import time
RandNo = random.randint(0, 100)
def Guess():
    print("You have 10 chances")
    n = 10
    i = 1
    while i <= n:
        Guess = int(input("Geuss the number: "))
        if Guess == RandNo:
            print("You Geussed Right")
            print("You win!!!")
            break
        elif (10 - i) == 0:
            print(end = "")
        elif Guess > RandNo:
            print(f"You have {10-i} chances left")
            print("Enter smaller number")
        elif Guess < RandNo:
            print(f"You have {10-i} chances left")
            print("Enter bigger number")
        i = i + 1
        if i == 11:
            print("You have no chances left!!")
            time.sleep(1)
            print("You lost!")
    
print("Welcome to Guess Number Game")
time.sleep(1)
print("Lets Start!")
time.sleep(1)
Guess()