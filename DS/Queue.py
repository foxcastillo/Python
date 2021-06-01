# Queue

# Queue is a FIFO data structure - - first-in, first-out.
# Deque is a double-ended queue, but we can use it for our queue.
# We use append() to enqueue an item, and popleft() to dequeue an item.
# See Python docs for deque.
"""
from collections import deque
my_queue = deque()
my_queue.append(5)
my_queue.append(10)
print(my_queue)
print(my_queue.popleft())

"""

# Python Single-ended Quque wrapper class using deque
from collections import deque

class Queue():
    def __init__(self):
        self.queue = deque() # inputter
        self.size = 0

    def enqueue(self, item):
        self.queue.append(item) # adds element
        self.size += 1

    def dequeue(self, item):
        if self.size > 0:
            self.size -= 1
            return self.queue.popleft() # removes element
        else:
            return None

    def peek(self):
        if self.size > 0:
            ret_val = self.queue.popleft() # peek/look
            queue.appendleft(ret_val)
            return ret_val
        else:
            return None

    def get_size(self):
        return self.size # outputter
    
# Maxheap

class MaxHeap:
    def __init__(self, items=[]):
        super().__init__()
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self.__floatUp(len(self.heap) - 1)

    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index//2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)

    def __str__(self):
        return str(self.heap)


m = MaxHeap([95, 3, 21])
m.push(10)
print(m)
print(m.pop())
print(m.peek())
