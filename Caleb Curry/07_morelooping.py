languages = ["Python", "C++", "Java", "Perl", "C#"]

for language in languages:
    if language == "Python":
        print(language, "is found")
        break
    
for language in languages:
    if language == "C++":
        print(language, "is found")
        break
    print("over.")
    
# Continue
print("searching for Java:")
for language in languages:
    if language == "Java":
        print(language + " found")
        continue
    print(language + ": Not What we are looking for...")


# else instead of continue (Method #2)
print("Searching for Perl:")
for language in languages:
    if language == "Perl":
        print(language, "is found")
    else:
        print(language + ": Not What we are looking for...")

# how to do nothing
for x in range(0, 10):
    pass

# Else with for
for i in range(0,10):
    print(i, end=" ")
else:
    print("Done") # counts range and ends with Done
    
# This can be useful for a failed search as an example because it will not be hit with break
for language in languages:
    if language == "Texas":
        print(language + " found")
        break
else:
    print("Nope.")
    
# While loop
i = 0 # inititalize
while(i < 10):
    print(i, end=" ")
    i += 1 # update
print()


