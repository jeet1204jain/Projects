Contacts = {
    "Jeet" : 8484901842
}

class SaveContact():
    Name = ""
    Number = 000
NewContacts = SaveContact()

f = open('co.txt', 'a+') 

def AddContact():
    for i in range(1, (n + 1)):
        EnterName = input("Enter name: ")
        EnterNumber = int(input("Enter number: "))
        NewContacts.name = EnterName
        NewContacts.number = EnterNumber
        for i in range(1):
                content = f.read()
                f.write(f"{NewContacts.name} : {NewContacts.number}\n")
                print("Successfully added!!!")
        

n = int(input("How many numbers You want to add: "))
AddContact()