# logic / booleans

happy = True
print(happy) # will print True

print(5 > 3) # will print True
age = 21 # variable
print("age >= 21?", age >= 21) # a True statement

me = 'Edgar'
you = 'a homie'

print("me == you?", me == you) # a False statement

# if statement
#First, the if statement.
print("What's your name?")
name = input()
print("what's your age?")
age = int(input())

if name == "Edgar":
    print("Hey, Edgar..What's up homie?")

# examples:

# Bad:
"""
if age > 100:
    print("WOW!")
print("You are so old")  # executes EVERY time

# Good:
if age > 100:
    print("WOW!")
    print("You are so old")
"""

# if elif else
if age > 100:
    print("you're old")
elif age > 120:
    print("dawg?")
else:
    print("you're good for now...")
    
# conditions
Edgar_is_homie = False
if Edgar_is_homie == True:
    print("wanna be friends?")
else:
    print("who are you? get away.")
    
# logical operators
thunder = False
lightning = True

if lightning or thunder:
    print("Don't go outside") 
# must be fully true and can't have one false or everything will be false.

car_nice = True
on_sale = False

if car_nice and on_sale:
    print("must buy") # will not execute