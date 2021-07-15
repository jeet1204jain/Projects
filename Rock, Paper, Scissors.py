import random
#Rock, Paper, Scissors

def game(comp, you):  
    if comp == 'Rock':
        if you == 'Paper':
            return True
        elif you == 'Scissors':
            return False
    elif comp == 'Paper':
        if you == 'Scissors':
            return True
        elif you == 'Rock':
            return False
    elif comp == 'Scissors':
        if you == 'Rock':
            return True
        elif you == 'Paper':
            return False
    elif you == comp:
        return None


rand = random.randint(1, 3)

if rand == 1:
    comp = 'Rock'
elif rand == 2:
    comp = 'Paper'
elif rand == 3:
    comp = 'Scissors'

print("Computer has chosen, now your turn")
you = input("Choose Rock , Paper , Scissors: ")
print(f"Computer chose {comp}")
print(f"You chose {you}")

a = game(comp, you)

if a == True:
    print("You win")    
elif a == None:
    print("A TIE")
elif a == False:
    print("You lose")

game(comp, you)