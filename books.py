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
        self.books.append({
            'name':name,
            'author':author,
            'read':False})
    # def view_books(self):
    #     for book in books :
    #         #self.list_books[book]
    #         print(book['name'])

    def list_books(self):
        for i in self.books :

            print(f"Name: {i['name']}")
            print(f"Author: {i['author']}")
            print(f"Read: {i['read']}")
    def edit_book(self,name):
        n = next(l for l in self.books if l['name']==name)
        print(n['read'])
        n['read']=True
        #self.list_books()
        # n['read']=True
        # print(n['read'])
        # self.list_books()

        # for book in self.books:
        #    if(book['name']==name):
        #        book['read']= True
        #         print(f"Author: {book['author']}")
        #         print(f"Read: {book['read']}")

            #     choice = input("do you want to save changes(y/n)")
            #     if choice == 'y':
            #         self.books.append({book['name'], book['author'], book['read']})

    def delete_book(self,name):

        n = next(l for l in self.books if l['name']==name)
        # del n['name']
        # del n['author']
        # del n['read']
        self.books.remove(n)

        # self.newlist = [book for book in self.books if book['name'] != name]
        # print(self.newlist)
        #self.list_books()
        #print(self.newlist)
def menu():
    print("Book Store")
    print("A     Add a book")
    print("V     View books list")
    print("E     Edit a book")
    print("D     Delete a book")
    print("Q     Quit")

menu()

bs = BookStore()
while(1):
    choice = input("Enter your choice  ").strip()
    if choice.upper() == 'A':
            bs.addbook()
            print(bs)
            bs.list_books()
            menu()

    elif choice.upper() == 'V':
           print(bs)
           bs.list_books()
           menu()

    elif choice.upper() == 'E':
            name = input("enter a book name to mark as read")
            bs.edit_book(name)
            print(bs)
            bs.list_books()
            menu()

    elif choice.upper() == 'D':
            name = input("enter a book name to delete")
            bs.delete_book(name)
            print(bs)
            bs.list_books()
            menu()
    elif choice.upper() == 'Q':
        exit(0)
        break

    else:
            print("Please choose options from the menu")
            menu()







