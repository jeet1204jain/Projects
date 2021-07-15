import random
import time
def Password():
    symbols_alphabet = ['!', '#', '$', '%', '^', '*']
    upper_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lower_alphabet1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l' 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    lower_alphabet2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l' 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    lower_alphabet3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l' 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    lower_alphabet4 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l' 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    number_1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    number_2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    number_3 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    number_4 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    symbols = random.choice(symbols_alphabet)
    upper = random.choice(upper_alphabet)
    lower1 = random.choice(lower_alphabet1)
    lower2 = random.choice(lower_alphabet2)
    lower3 = random.choice(lower_alphabet3)
    lower4 = random.choice(lower_alphabet4)
    number1 = random.choice(number_1)
    number2 = random.choice(number_2)
    number3 = random.choice(number_3)
    number4 = random.choice(number_4)
    print(symbols + "" + upper + "" + lower1 + "" + lower1 + "" + lower2 + "" + lower3 + "" + lower4 + "" + number1 + "" + number2 + "" + number3 + "" + number4)

print("Welcome to Password Generator")
time.sleep(1)
gene = input("If you want to generate password press 'g': ")
if gene == "g":
    print("So lets start!")
    time.sleep(1)
    print("Password: ")
    Password()
    time.sleep(1)
    print("Thank You!!!")
elif gene != "g":
    print("Exited")