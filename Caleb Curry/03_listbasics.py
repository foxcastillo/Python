# what's a list? lol

import copy
ages = [20, 25, 20] # this is a list
names = ["Edgar, Steven, Jose"] # this is also a list
food = ['chicken', 'pollo', 1738] # did you know that this is also a list
print(ages)
print(names)
print(food)

# indexing (again)
print(ages[0]) # grabs the first element

# how to update a list element
ages[0] = 5
ages[1] = 10
ages[2] = 15
print(ages)  # Updated!

# What about slicing?
print(ages[1:]) # It works! #grabs all elements except for the first element lol.

ages[1:] = [6, 7]
print(ages)  # it worked?
# this method helps you with updating data from list in a quicker way.

# how to copy list?
names = ['Edgar', 'Steven', 'Jose']
names2 = names[:] # proper way instead of (names2 = names) way.
print(names2)

# here's another method to copy lists
names1 = ['Edgar', 'Steven', 'Jose']
names2 = names1.copy()
names2[0] = 'goat status'
print(names2)

# Nested list
my_favorite_things = ["music", 18, ["HBO Max", "Hulu"]] 
# The third element is actually a list itself.

streaming = my_favorite_things[2]
print(streaming) # we get the second list
print(streaming[1]) # we grab the Hulu element from the second list

# a more useful way of grabbing an element from a nested list is like so:
print(my_favorite_things[2][1]) # goat method lol.
#first [] is outer list. second [] is inner list.

#This can be repeated even deeper.
nested_list = [[[[["deep dive"]]]]]
print(nested_list[0][0][0][0][0])  # Got it!

# shallow copy
# This means that any complex types will not be copied but rather available in both
# The easiest way to understand this is with an example.

my_favorite_things = ["music", 18, ["HBO Max", "Hulu"]]
my_favorite_things2 = my_favorite_things.copy()

# now, modify the original
my_favorite_things[2][0] = "Spotify"
print(my_favorite_things2)  # now has Spotify instead of HBO Max

# combining lists
msg = "he" "llo" # '+' is optional in strings
print(msg)

good = ['chicken', 'pollo', 'pollo loco']
bad = ['chocolate', 'chocalate chicken', 'chocolate soup']
average_good = good + bad
print(average_good)