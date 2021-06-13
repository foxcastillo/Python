# create a class and __init__

class Book():
    pass

book = Book()
print(book)  # we get <__main__.Book object at 0x7fe3b9636a60>

# When we say Book() we are instantiating a new object
# This object iws assigned to the book variable
# Printing it gives us the type and memory location

# second method:
print(type(book))  # we get <class '__main__.Book'>

# Then...
class Book():
    def __init__(self, title):
        self.title = title
        
# consider this the constructor, or the function that is invoked when we create a book.
# self refers to the book being created 
# and we don't have to worry about passing that, it's implicit...
# Title is passed in as an argument, and assigned to self.title (the title of the book)
 
# methods
class Book():
    def __init__ (self, title, pages):
        self.title = title
        self.pages = pages
        
    def log(self):
        print(f"{self.title} is {self.pages} pages long.")
        
    def is_short(self):
        if self.pages < 100:
            return True
        
book = Book("are you my mother", 72)
book.log()

# prints out: are you my mother is 72 pages long.

# class level variables

# self refers to the object things are being invoked on,
# When we create an object. __init__ assigns stuff to self
# That allows each object to have attributes.

class Book():
    favs = [] # class
    
    def __init__ (self, title, pages):
        self.title = title
        self.pages = pages
        
    def log(self):
        print(f"{self.title} is {self.pages} pages long.")
        
    def is_short(self):
        if self.pages < 100:
            return True
    
book = Book("are you my mother?", 72) # title and number of pages
book2 = Book("The Digging-est Dog", 72)

Book.favs.append(book) # add books to the list
Book.favs.append(book2)

print(Book.favs)

#To save save space we are combing the code for all three of these sections.

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

    #If should immutable, you could do something like this.
    #This replaces __hash__ = None
    def __hash__(self):
        # xor with hash of attributes
        return hash(self.title) ^ hash(self.pages)
        #from Mastering Object-Oriented Python


book = Book("Are You My Mother", 72)
print(book)
equal_book = Book("Are You My Mother", 72)
print("Are they considered equal?", book == equal_book)  # yep
print("Are they the same object?", book is equal_book)  # nope
book2 = Book("The Digging-est Dog", 72)

print(hash(book), hash(book2))

print("old hash", hash(book))
book.title = "new"
print("new hash", hash(book))  # BAD!!!
#Hashes shouldn't change
