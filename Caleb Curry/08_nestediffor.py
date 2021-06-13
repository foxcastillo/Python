# The only form of nesting we've encountered so far was an if statement within a loop.
languages = ["Python", "C++", "Java", "Perl", "C#"]

for language in languages:
    if language == "C#":
        print(language + " found")
        break

# breaks the operation / not good for us
for language in languages:
    if language == "C#":
        print(language, "is found")
    break

# Nested if

logging = True
logging_in = True
name = "Edgar"

if logging_in:
    if logging:
        print(name, "is logging in...") # log console, file, or db
    print(f'Welcome {name}')
    
# Intro to nested for
for i in range(4):
    for j in range(5):
        print(j, end=" ")
    print() # go to next line print 1-4 five times.