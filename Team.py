import random
def TeamMaker():
    Team_A = ["Rishi"]
    Team_B = ["Shreeraj"]
    rand1 = random.randint(1, 2)
    rand2 = random.randint(1, 2) 
    if rand1 == 1:
        Team_A.append("Jeet")
        Team_B.append("Jinisha")
    elif rand1 == 2:
        Team_A.append("Jinisha")
        Team_B.append("Jeet")

    if rand2 == 1:
        Team_A.append("Dhruv")
        Team_B.append("Aryan")
    elif rand2 == 2:
        Team_A.append("Aryan")
        Team_B.append("Dhruv")
    print(f"Team_A: {Team_A}")
    print(f"Team_B: {Team_B}")

TeamMaker()