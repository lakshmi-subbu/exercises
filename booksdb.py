import sqlite3 as lite
import sys
try:
    con = lite.connect('books1.db')
    cursor = con.cursor()
    cursor.execute('CREATE TABLE  if not exists books1( name text not null ,author  text not null,read boolean)')
    #cursor.execute("insert into employees values (1,'subbu',30, 'america')")
     #con.commit()
    # cursor.execute("select * from employees")
    # data =cursor.fetchall()
    # print(data)
    # for rec in data:
    #     print(f"name is {rec[1]}")
    #     print(f"age is {rec[2]}")
    #     print(f"address is {rec[3]}")
    # con.close()
except Exception as e:
    print("failed")
    print(e)
def addbooks ():
    name = input("Enter book name: ")
    author = input("Enter author\'s name")
    read = input("mark read (True/False)")
    cursor.execute("insert into books1 values(?,?,? )",(name,author,read))
    con.commit()
    #con.close()
def listbooks():
    cursor.execute("select * from books1")
    data = cursor.fetchall()
    if data is None :
        print("No record found")
    else:
        print(data)
        for rec in data:
             print(f"name is {rec[0]}")
             print(f"age is {rec[1]}")
             print(f"read is {rec[2]}")
             print("-"*25)
    con.commit()
def editbooks():
    name = input("Enter the book name to mark as read").strip()
    cursor.execute("select *  from books1 where name = ?",(name,))
    data = cursor.fetchone()
    if data is None :
        print("No record found")
    else:
        print(f"name is {data[0]}")
        print(f"author is {data[1]}")
        print(f"read is {data[2]}")
    #data[2]=True
        cursor.execute("update books1 set read = ? where name =?",(True,name))
        listbooks()
    #print()
def deletebooks():
    name = input("Enter the book name to delete").strip()
    cursor.execute("select *  from books1 where name = ?", (name,))
    data = cursor.fetchone()
    if data is None:
        print("No record found")
    else:

        cursor.execute("delete from books1 where name = ? ",(name,))
        print("deleted successfully")
        con.commit()

def menuList():
    print("Book Store")
    print("A     Add a book")
    print("V     View books list")
    print("E     Edit a book")
    print("D     Delete a book")
    print("Q     Quit")
menuList()
while(1):
    #menuList()
    choice = input("Enter your choice").strip()
    if choice.upper() == 'A':
        addbooks()
        listbooks()
        menuList()
    elif choice.upper() == 'V':
        listbooks()
        menuList()
    elif choice.upper() == 'E':

        editbooks()
        menuList()
    elif choice.upper() == 'D':

        deletebooks()
        #listbooks()
        menuList()
    elif choice.upper() == 'Q':
        exit(0)
        break
    else:

        print("Please choose options from the menu")
        menuList()

#addbooks()
#listbooks()
#editbooks()
#deletebooks()
