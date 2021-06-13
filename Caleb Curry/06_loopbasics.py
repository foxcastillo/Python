languages = ['Python', 'C', 'Java']

for x in languages:
    print(x) # will run all the elements from the list then will break.
    
# The Variable name is irrelavant
for language in languages:
    print(language) 
    
# print without newline
print("One", end=' ')
print("Line") # One Line

# This is useful for loops where you don't want to spam the terminal
for language in languages:
    print(language, end=" ")
print() # Python C Java

# Range function
for i in range(10):
    print("loading...", end=" ")
print() # prints loading 10 times

for i in range(10):
    print(i, end=" ")
print() # prints 0 through 9

# Range start position
for i in range(1, 11):
    print(i, end=" ")
print() # prints 11 through 10

# we can start from anywhere
for i in range(5, 7):
    print(i, end=" ")
print() # prints 5 and 6

# Range Step
for i in range(9, -1, -1):
    print(i, end=" ")
print() # prints 9 to 0 (reverse)

# Sum of list
# Sum of numbers 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print(sum(range(1, 11))) # total of 55

# List from range
numbers = list(range(1,11))
print(numbers) 

# for loop with index
languages = ['python', 'C', 'Java']
for i in range(len(languages)):
    print(i, languages[i])
