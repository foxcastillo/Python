# Stack is a LIFO data structure -- last-in, first-out.
# Use append() to push an item onto the stack.
# Use pop() to remove an item.

my_stack = list()
my_stack.append(4)
my_stack.append(7)
my_stack.append(12)
my_stack.append(19)
print("First stack:", my_stack)

print(my_stack.pop())
print(my_stack.pop())
print("Second Stack:", my_stack)

# Stack using List with a Wrapper Class

# We create a Stack class and a full set of Stack methods.
# But the underlying data structure is really a Python List.
# For pop and peek methods we first check whether the stack is empty, to avoid exceptions. 

class Stack():
    def __init__(self):
        self.stack = list()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        else:
            return None

    def __str__(self):
        return str(self.stack)

# Test Code for Stack Wrapper Class

my_stack = Stack()
my_stack.push(1)
my_stack.push(3)
print(my_stack)
print(my_stack.pop())
print(my_stack.peek())
print(my_stack.pop())
print(my_stack.pop())
