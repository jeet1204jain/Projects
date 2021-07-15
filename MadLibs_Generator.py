import time
import keyboard
import random

print("----------------------------Welcome to MadLibs Generator----------------------------")
time.sleep(1)
g = input("If you don't know how to play, press 't' ; or if you know how to play, press 'k': ")

if g == "t":
    print("1.Its an multiplayer game")
    time.sleep(2)
    print("2.First person will enter a word, then second and so on(Dont tell any one your entered word)")
    time.sleep(2)
    print("3.After all are done, then first person will enter a question and word told by last perosn will be its answer")
    time.sleep(2)
    print("Its same like chinese whisper game")
    time.sleep(2)
elif g == "n":
    print("Ok, then lets start")
    
p = int(input("How many players are there: "))


def Final():
    for i in range(1, p + 1):

        RandNo = random.randint(1, 6)

        if RandNo == 1:
            q = "What is your name?"
        elif RandNo == 2:
            q = "What do you eat?"
        elif RandNo == 3:
            q = "What is your favourite?"
        elif RandNo == 4:
            q = "What is the time?"
        elif RandNo == 5:
            q = "What do you like?"
        elif RandNo == 6:
            q = "You are interested in?"


        w = input(f"Enter word: ")

        a = print(f"{q} = {w}")
        print(a)
        time.sleep(1)
    print("Game Over!!!")

Final()