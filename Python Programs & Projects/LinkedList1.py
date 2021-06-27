# Edgar Castillo / Github: https://github.com/hellocastillo
# Copyright (c) 2021 Edgar Castillo

# Linked List
# Node Class

class Node:

    def __init__(self, d, n=None, p=None):
        self.data = d
        self.next_node = n
        self.prev_node = p

    def __str__(self):
        return ('(' + str(self.data) + ')')


# Linked List Class
class LinkedList:

    def __init__(self, r=None):
        self.root = r
        self.size = 0

    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1

    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                return d
            else:
                this_node = this_node.next_node
        return None

    def remove(self, d):
        this_node = self.root
        prev_node = None

        while this_node is not None:
            if this_node.data == d:
                if prev_node is not None:  # data is in non-root
                    prev_node.next_node = this_node.next_node
                else:  # data is in root node
                    self.root = this_node.next_node
                self.size -= 1
                return True    # data removed
            else:
                prev_node = this_node
                this_node = this_node.next_node
        return False  # data not found

    def print_list(self):
        this_node = self.root
        while this_node is not None:
            print(this_node, end='->')
            this_node = this_node.next_node
        print('None')

# Linked List Test code
myList = LinkedList()
myList.add(5)
myList.add(8)
myList.add(12)
myList.print_list()

print("size="+str(myList.size))
myList.remove(8)
print("size="+str(myList.size))
print(myList.find(5))
print(myList.root)

# Circular linked List

class CircularLinkedList:

    def __init__(self, r=None):
        self.root = r
        self.size = 0

    def add(self, d):
        if self.size == 0:
            self.root = Node(d)
            self.root.next_node = self.root
        else:
            new_node = Node(d, self.root.next_node)
            self.root.next_node = new_node
        self.size += 1

    def find(self, d):
        this_node = self.root
        while True:
            if this_node.data == d:
                return d
            elif this_node.next_node == self.root:
                return False
            this_node = this_node.next_node

    def remove(self, d):
        this_node = self.root
        prev_node = None

        while True:
            if this_node.data == d:   # found
                if prev_node is not None:
                    prev_node.next_node = this_node.next_node
                else:
                    while this_node.next_node != self.root:
                        this_node = this_node.next_node
                    this_node.next_node = self.root.next_node
                    self.root = self.root.next_node
                self.size -= 1
                return True     # data removed
            elif this_node.next_node == self.root:
                return False    # data not found
            prev_node = this_node
            this_node = this_node.next_node

    def print_list(self):
        if self.root is None:
            return
        this_node = self.root
        print(this_node, end='->')
        while this_node.next_node != self.root:
            this_node = this_node.next_node
            print(this_node, end='->')
        print()

# Circular Linked List Test code

cll = CircularLinkedList()
for i in [5, 7, 3, 8, 9]:
    cll.add(i)

print("size="+str(cll.size))
print(cll.find(8))
print(cll.find(12))

my_node = cll.root
print(my_node, end='->')
for i in range(8):
    my_node = my_node.next_node
    print(my_node, end='->')
print()

