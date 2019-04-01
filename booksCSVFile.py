import csv
import os
class BookStore :


    def __init__(self):
        self.books = []
        self.newlist  = []
    def __str__(self):
        return f"The number of books in this bookstore is {len(self.books)}"
    def __getitem__(self, item):
        return self.books[item]
    def __repr__(self):
        return f"books:{self.books}"
    def addbook(self):
        name = input("Enter book name: ")
        author = input("Enter author\'s name")
        read = input("mark read (True/False)")
        #self.books.append(name,author,read)
        if not os.path.exists("C:\\Users\\subbulakshmi\\PycharmProjects\\bookstore\\books.csv"):
             with open('booksStore.csv', 'w+', newline='') as csvfile:
                myFields = ['Name', 'Author', 'Read']
                csvwriter = csv.DictWriter(csvfile,fieldnames=myFields)
                csvwriter.writerow('Name','Author','Read')
                csvwriter.writerow({'Name':name,'Author':author,'Read':read})

        else:
            with open('booksStore.csv', 'a', newline='') as csvfile:
                myFields = ['Name', 'Author', 'Read']
                csvwriter = csv.DictWriter(csvfile,fieldnames=myFields)
                csvwriter.writerow({'Name': name, 'Author': author, 'Read': read})

            #csvwriter.writerow()
            #csvfile.close()



    def list_books(self):
        csv.register_dialect("mydialect", delimiter='|', skipinitialspace=True)
        with open("booksStore.csv", "r") as csvfile:
            reader = csv.reader(csvfile, dialect='mydialect')
            for row in reader:
                print(row)



    def edit_book(self,name):

        with open("booksStore.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            data =[row for row in reader if row[0]==name]
            n = data[0][0]
            a = data[0][1]
            r = data[0][2]
            print(n)
            print(a)
            print(r)
            r = True
            if not os.path.exists("C:\\Users\\subbulakshmi\\PycharmProjects\\bookstore\\booksEdit.csv"):
                with open('booksStore.csv', 'w+', newline='') as csvfile:
                    myFields = ['Name', 'Author', 'Read']
                    csvwriter = csv.DictWriter(csvfile, fieldnames=myFields)
                    csvwriter.writerow('Name', 'Author', 'Read')
                    csvwriter.writerow({'Name': n, 'Author': a, 'Read': r})
            else:
                with open('booksEdit.csv', 'a', newline='') as csvfile:
                    myFields = ['Name', 'Author', 'Read']
                    csvwriter = csv.DictWriter(csvfile,fieldnames=myFields)
                    csvwriter.writerow({'Name': n, 'Author': a, 'Read':r})

                    #data['read']=True



    def delete_book(self,name):
        with open("booksStore.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            data =[row for row in reader if row[0]==name]
            n = data[0][0]
            a = data[0][1]
            r = data[0][2]
            if not os.path.exists("C:\\Users\\subbulakshmi\\PycharmProjects\\bookstore\\booksEdit.csv"):
                with open('booksStore.csv', 'w', newline='') as csvfile:
                    myFields = ['Name', 'Author', 'Read']
                    csvwriter = csv.DictWriter(csvfile, fieldnames=myFields)
                    csvwriter.writerow('Name', 'Author', 'Read')
                    csvwriter.writerow({'Name': n, 'Author': a, 'Read': r})
            else:
                with open('booksDelete.csv', 'a', newline='') as csvfile:
                    myFields = ['Name', 'Author', 'Read']
                    csvwriter = csv.DictWriter(csvfile,fieldnames=myFields)
                    csvwriter.writerow({'Name': n, 'Author': a, 'Read':r})



def menuList():
    print("Book Store")
    print("A     Add a book")
    print("V     View books list")
    print("E     Edit a book")
    print("D     Delete a book")
    print("Q     Quit")

bs = BookStore()
menuList()

while(1):
    choice = input("Enter your choice").strip()
    if choice.upper() == 'A':
        bs.addbook()
        bs.list_books()
        menuList()
    elif choice.upper() == 'V':
        bs.list_books()
        menuList()
    elif choice.upper() == 'E':
        name = input("enter a book name to mark as read")
        bs.edit_book(name)
        bs.list_books()
        menuList()
    elif choice.upper() == 'D':
        name = input("enter a book name to delete")
        bs.delete_book(name)
        bs.list_books()
        menuList()
    elif choice.upper() == 'Q':
        exit(0)
        break
    else:

        print("Please choose options from the menu")
        menuList()


