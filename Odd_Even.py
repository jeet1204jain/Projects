import time
import random

def OE():
    print("--------------------------------------Welcome-----------------------------------")
    time.sleep(0.5)
    print("Lets Play!!!")
    time.sleep(0.5)

    oddoreve = input("You want odd or even: ")

    comp = random.randint(1, 6)
    number = int(input("Enter your number: "))
    total = number + comp

    if (total%2 == 0):
        final = "Even"
    elif (total%2 != 0):
        final = "Odd"
    
    print(f"You entered {number}")
    time.sleep(1)

    print(f"Computer entered {comp}")
    time.sleep(1)

    print(f"The sum is {total}")
    time.sleep(1)

    if final == oddoreve:
        print("You win!!!")
    else:
        print("You lose!!!")

OE()