import json,codecs
import  os
def menu():
    print("Favorite Movie Collection")
    print("Please Choose")
    print("A     Add a book")
    print("V     View books")
    print("E     Edit book")
    print("X     Exit")

def addbooks():
    name = input("Enter book name: ")
    author = input("Enter author\'s name")
    #read = input("mark read (True/False)")

    books ={'name':name,'author:':author,'read':False}
    with open('booksStores.json', 'w',) as jsonFile:
         json.dumps(books)
    print(json.dumps(books))

def listbooks():
    with open("booksStores.json", "r") as jsonFile:
        data = jsonFile.read()
        obj = json.loads(data)
        print("Name: " + obj["name"])
        print("Author: " + obj["author"])
        print("Read: " + obj["read"])
menu()
while(1):
    choice = input("Enter your choice").strip()
    if choice.upper() == 'A':
        addbooks()
        menu()

    elif choice.upper() == 'V':
        listbooks()
        menu()
    elif choice.upper() == 'S':

        menu()
    elif choice.upper() == 'X':
        exit(0)
        break
    else:
        print("Please choose options from the menu")
        menu()

