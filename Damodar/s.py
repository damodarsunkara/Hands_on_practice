class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.available=True

    def __str__(self):
        return f'the book  with {self.title} written by {self.author} '
class Library:
    def __init__(self):
        self.book=[]
    def _add(self,add):
        
        self.book.append(add)

    def is_display(self):
        for book in self.book:
            
           print(book)
    def is_free(self,title):
        
        for book in self.book:
            if book.title.lower()==title.lower():
                print("yes book is available")
                return book.available
      
    def borrow(self,title):
        for book in self.book:
            if book.title.lower()==title.lower():
                if book.available:
                    book.available=False
                    print("the book u borrowing is {self.book)")
                    return
                else:
                    print("the book was {self.book} borrowed already")
                    return
        print("the book was not found")
    def _return(self,title):
        for book in self.book:
            if book.title.lower()==title.lower():
                if not book.available:
                    book.available=True
                    print("The book u r returning is {self.book]")
                    return
                else:
                    print("the book is not borrow:")
                    return
                    
        print("book was not found")
                          
                
            

def main():            
    
    li=Library()
    li._add(Book("hall of frame:","johm"))
    li._add(Book("hall","johm"))
    while True:
        user=int(input("enter u r option: 1.add \n2.display \n3.available \n4.borrowing \n5.returning \n6.exit  \n\n"))
        if user == 2:
            li.is_display()
        elif user == 3:
            title=input("enter the book title ")
            li.is_free(title)
            
        elif user ==4:
            title=input("enter the title of the book")
            li.borrow(title)
        elif user== 5:
            title=input("enter the book title")
            li._return(title)

        elif user==6:
            break
        else:
            print("enter the valid choice")


if __name__== "__main__":
     main()
