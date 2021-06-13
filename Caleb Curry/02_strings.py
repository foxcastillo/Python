me = 'Edgar'
print(me)
print("\n") # escape character

# passing multiple arguments to print
you = 'Subscriber'
print(me, you)

single_quotes = 'She said "Hi"'
print(single_quotes)

double_quotes = "She said \"Hi\""
print(double_quotes)

single_quotes = 'I\'m learning!'
print(single_quotes)

double_quotes = "I'm learning!"
print(double_quotes)

# Use a '+' to concatenate 
msg = me + " + " + you
print(msg)

# You can also use multiline string
print("""Name: Edgar
Age: 18""")

# indexing
msg = "This is a very important message."
print(msg[5]) # will print out 'i'.

# indexing is zero based. This means 0 will get the very first character:
print(msg[0]) # will print out 'T'

# This value is returned and can be assigned to a variable or used in an expression
first_letter = msg[0]
print(first_letter + "acos") # will print out 'Tacos'

# You can also index from the right.
period = msg[32]  # from left
print(period) # will print out '.'

period = msg[-1]  # from right
print(period) # easier method and will print out '.'

# slicing
#repeating this for ease of reading:
msg = "This is a very important message."

# this will get 2 characters (from index 1 - 3 with 3 not included...we are left with index 1 and 2.
print(msg[1:3])  # hi

# You can also leave off first to start at beginning
# or leave off second to go to end
print(msg[:5])  # print index 0-4 (because 5 is excluded, remember)
print(msg[1:])  # from index 1 to end

# We can also use negatives. Here is how you get the last 8 characters:
print(msg[-8:])  # start 8 from right and go to end

# immutability
# Strings are immutable, meaning they can't change.
cant_change = "Java is my favorite!"

new = 'K' + cant_change[1:] # will replace 'J' wit 'K'
print(new)  # Kava is my favorite!

fav_language = "Python " + cant_change[5:]
print(fav_language)  # Python is my favorite!

coffee = cant_change[:8] + "actually coffee" # grab first 7 characters (index 8 not included.)
print(coffee)  # Java is actually coffee

coffee += " (contrary to popular belief)."
print(coffee) # Java is actually coffee (contrary to popular belief).

# string length
print(len(coffee)) # 53 characters in length

# first index is always len(variable[0])
# last index is always len(variable[-1])

#How to convert a number to a string
length = len(coffee)

print("Length is " + str(length)) # length is 53

# Examples

# Bad
msg = "length is", len(coffee)
print(msg)  # NOT WHAT WE WANTED!

# Good / Average
length = len(coffee)
msg = "length is " + str(length)
print(msg)

# Even Better / Professional
print("length is " + str(length))
