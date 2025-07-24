class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
    
    def borrow(self):
        if self.available:
            self.available = False
            print(f"The book '{self.title}' by {self.author} has been borrowed.")
        else:
            print(f"Sorry, '{self.title}' is already borrowed.")
    def return_book(self):
        if self.available:
            self.available = True
            print(f"The book '{self.title}' by {self.author} has been returned.")
        else:
            print("Thankyou for the free book")
book1 = Book("Deadly Hollow", "J.K. Rowling")
book2 = Book("Song of Ice and Fire", "George R.R. Martins")

book1.borrow()
book1.return_book()
print(f"Is the book available? {book1.available}")