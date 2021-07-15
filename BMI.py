import time
k = input("If you know what is BMI, then press 'k'\nIf you dont know what is BMI, press 'y': ")

if k == "y":
    print("1.BMI is a qunatity to measure whether you are underweight, normal, or overweight")
    time.sleep(1.5)
    print("2. Just put your height and weight")
    time.sleep(1)
    print("If your BMI is:\n<18.5 : Underweight\n18.5 - 25: Normal Weight\n25 - 29.9 = Overweight\n>29: Obessed")
    time.sleep(2)
    print("So lets start!!!")
    time.sleep(1)

def BMI():
    weight = float(input("Step 1: Enter Your Weight(kg): "))
    height = int(input("Step 2: Enter Your Height(cm): "))
    heightf = (height/100)
    heightf1 = (heightf * heightf)
    BMI = (weight/heightf1)
    
    print(f"Your BMI is {BMI}")
    if (BMI < 18.5):
        print("You are Underweight")
    elif (BMI > 18.5 and BMI < 25):
        print("You are Normal weighted")
    elif (BMI > 25 and BMI < 29.9):
        print("You are Overweight")
    elif (BMI > 29.9):
        print("You are Obessed")
        
BMI()