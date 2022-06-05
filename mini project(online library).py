class Library:
    def __init__(self,list,name):
        self.bookslist=list
        self.name=name
        self.lendlist={}

    def Displaybooks(self):
        print(f"We have following books in our library {self.name}")
        for book in self.bookslist:
            print(book)
    def Lendbook(self,user,book):
        if book not in self.lendlist.keys():
            self.lendlist.update({book:user})
            print ("Lender-Book database had been updated .you can enjoy the book now , THANK YOU")
        else:
            print (f" the book had been taken by {self.lendlist[book]}")
    def addbook(self,book):
        self.bookslist.append(book)
        print ("Book has been updated")
    def returnbook(self,book):
        self.lendlist.pop(book)
if __name__ == '__main__':
    Srijan=Library(['Deep Work','Rich Dad Poor Dad','autobiography of Sam Manekshaw','Python by Sumita Arora','C++ Basics'],"LibraryForGREATMINDS")
    while (True):
         print (f"Welcome to {Srijan.name}library .Enter your choice to continue")
         print("1.Display Books")
         print("2. Lend a book")
         print("3.add a book")
         print("4.return a book")
         user_choice=int(input())
         if user_choice==1:
             Srijan.Displaybooks()
         elif user_choice == 2:
             book =input("enter the book:")
             user=input("enter the name:")
             Srijan.Lendbook(book,user)
         elif user_choice == 3:
             book=input('enter the name of book you wanna add')
             Srijan.addbook(book,user)

         elif user_choice == 4:
            book = input('enter the name of book you wanna return')
            Srijan.lendlist.pop(book)
         else:
             print('enter valid choice')
         print("print q to quit and c to continue")
         userchoice = ""
         while (userchoice!='c' and userchoice!='q'):

           userchoice=(input())
           if userchoice=='c':
             continue
           elif userchoice=='q':
             exit()
