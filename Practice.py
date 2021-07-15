#num = int(input("enter number: "))
#for i in range(1, 11):
#     print(str(num) + "x" + str(i) + "=" + str(i*num))
#     print(f"{num}X{i}={num*i}")

#l1 = ["harry", "sohan", "sachin", "rahul"]
#
#for name in l1:
#    if name.startswith("s"):
#        print("Hello " + name)

#num = int(input("Enter number: "))
#i = 1
#while i <= 10:
#    print(str(num) + "X" + str(i) + "=" + str(i*num))
#    i = i + 1

#num = int(input("Enter number: "))
#prime = True
#for i in range(2, num): 
#    if(num%i == 0):
#        prime = False
#        break
#if prime:
#    print("Number is prime")
#else:
#    print("Number is not prime")

#num = int(input("Enter the number: "))
#factorial = 1
#for i in range(1, num+1):
#    factorial = factorial * i
#print(f"The factorial of {num} is {factorial}")

#num = int(input("Till which number you want sum: "))
#sum = 0
#for i in range(0, num+1):
#    sum = sum + i
#print(f"The total sum till {num} is {sum}")

#num = int(input("How many lines you want: "))
#for i in range(num):
#    print("*" * (i +1))


#n = int(input("How many lines you want: "))
#for i in range(n):
#    print(" " * (n-i-1), end="")
#    print("*" * (2*i+1), end="")
#    print(" " * (n-i-1))

n = int(input("Enter number: "))
if (n%2 == 0):
    print("Its is an even number")
else:
    print("It's an odd number")
