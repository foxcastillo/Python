"""
my_list = list(range(0,10))
my_list.append(10)
print("Step 1:(append)", my_list)

my_list.insert(2, 10)
print("step 2:(insert)", my_list)

my_list.pop()
print("step 3:(pop)", my_list)

my_list.remove(10)
print("step 4:(pop)", my_list)

"""
# Queue follows FIFO (First in, First Out)
# Stack follows LIFO (Last in, First Out)


from collections import deque

linked_list = deque()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
# print(linked_list)

queue = deque()

for i in range(0,5):
    queue.append(i) # adding an element at the beginning of the queue
    #print(queue)
    
for i in range(len(queue)): # removing the first element from queue
    queue.popleft()
    #print(queue)
    
stack = deque()

for i in range(0,5): # adding an element at the beginning of the stack
    stack.appendleft(i)
    #print(stack)

for i in range(len(stack)): #removing the first element from stack
    stack.popleft()
    #print(stack)

# custom linked list (for interviews lol)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Linked:
    def __init__(self):
        self.head = None

    def show(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next
