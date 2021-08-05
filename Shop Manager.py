import datetime
import time

Employees = ["Azhar", "Babloo", "Mahadu", "Yogesh"]

#class Employee():
#  Name = ""
#  Salary = 0
#  Work_Done = 0

#Azhar = Employee()
#Babloo = Employee()
#Mahadu = Employee()
#Yogesh = Employee()
#Azhar.name = "Azhar Sheikh"
#Babloo.name = "Taj Khan"
#Mahadu.name = "Mahadu"
#Yogesh.name = "Yogesh Jadhav"

def Function():
  print("What do you want to do")
  print("1. View Data")
  print("2. Enter Data")
  wtd = input("Enter: ")
  print(wtd)
  if wtd == 1:
    print("Your Data: ")
    with open("Shop Data.txt", "r") as rd:
      content = rd.read()
      print(content)
  elif wtd == 2:
    date = input(Enter today's date: ")
    for emply in Employees:
      wd = input("Enter work done today by {emply}: ")
      with open("Shop Data.txt", "w") as f:
        f.write(date)
        f.write({emply})
        f.write({wd})

Function()
