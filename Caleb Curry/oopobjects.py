class Book():
    favs = []  # class

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def is_short(self):
        if self.pages < 100:
            return true

    #What happens when you pass object to print?
    def __str__(self):
        return f"{self.title}, {self.pages} pages long"

    #What happens when you use ==?
    def __eq__(self, other):
        if(self.title == other.title and self.pages == other.pages):
            return True

    #It's approriate to give something for __hash__ when you override __eq__
    # #This is the recommended way if mutable (like it is here):
    __hash__ = None

# passing by object reference

book = Book("Where is my Mother", 72)
print(book)  # Where is my Mother, 72 pages long

def modify(self): # changed the book's title
    book.title = "changed noob"

modify(book)
print(book)

# What is we print ID to follow?
def modify(book):
    print(id(book))
    book.title = "Chaged noob"
    print(id(book)) 