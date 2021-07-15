print("-------------------------------Welcome TO Library---------------------------------------")
Books = ["Mahabharata", "Ramayan", "Story Of Jeet Jain", "Grandma Stories", "Harry Potter 1"]
Books.sort()
print("1.Take Book\n2.Return Book\n3.View Library\n4.Exit Library")
def Take_Book():
            if q == "take":
                print(f"Books Available {Books}")
                take = input("Which Book You Want: ")
                if take in Books:
                    print(f"{take} is choosen\nThanks For Shopping!!!")
                    Books.remove(take)
                elif take not in Books:
                    print("You entered wrong name of book")
                    take1 = input("Type again: ")
                    if take1 in Books:
                        print(f"{take1} is chosen\n Thanks for Shopping")
def Return_Book():
        if q == "return":
            give = input("Which book you want to return: ")
            Books.append(give)
            print("Thanks!!!")
            print(Books)
def View_Library():
        if q == "view":
            print(f"Books available: {Books}")
            q1 = input("Do you want take to take any book: ")
            if q1 == "yes":
                take1 = input("Which book you want: ")
                if take1 in Books:
                    print(f"{take1} is choosen\nThanks For Shopping!!!")
                    Books.remove(take1)
                elif take1 not in Books:
                    print("You entered wrong name of book")
                    take1 = input("Type again: ")
                    if take1 in Books:
                        print(f"{take1} is chosen\n Thanks for Shopping")
            elif q1 == "no":
                print("Ok!")
def Exit_Library():
        if q == "exit":
            print("Exited Library!")

q = input("What do you want to do: ")
if q == "take":
    Take_Book()
elif q == "return":
    Return_Book()
if q == "view":
    View_Library()
elif q == "exit":
    Exit_Library()