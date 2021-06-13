# nested loops
for i in range(4):
    for j in range(5):
        print(j, end=" ")
    print()

for i in range(4):
    print("iteration ", str(i), end=" ")
    for j in range(5):
        print(j, end=" ")
    print() # prints: "iteration: 0 0 1 2 3 4"...

# outer loop variables in inner range() - triangles
for i in range(10):
    for j in range(i, 10):
        print(j, end=" ")
    print() # does a triangle 
    
# nested while
# print 0-4, 4 times
i = 0
while i < 4:
    j = 0
    while j < 5:
        print(j, end=" ")
        j += 1
    print()
    i += 1