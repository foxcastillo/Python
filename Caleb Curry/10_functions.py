# how to create a function
def greet():
    print("Hello")
    print("welcome, Edgar")
greet() # prints
greet() # prints(2)
greet() # prints(3)

# arguments and parameters
def greet(name): # name is a parameter
    print('hello')
    print('welcome, ', name)

greet('Edgar') # Edgar is the argument

# return
def greet(name):
    if name == 'Edgar':
        return
    else:
        print('hello')
        print('welcome, ', name)
    
greet('Edgar')

# return values
def greet(name):
    if name == 'Jose':
        return 'Go away'
    return "hello ", name, "Welcome to my app"

returned = greet('Edgar')
print(returned) 