
# Authors: Andres Greene
#         Raquel Garcia
#         Laureano Griffin
#         Josue Gonzalez-Picasso

class Dynamic_queue:

    # Constructor
    def __init__(self, value=10):
        # Initializes attributes
        self.elements = []*value
        # self.iHead = 0
        # self.iTail = 0
        # self.entryCount = 0
        # Sets capacity equal to 1 if the value is equal to zero or lower
        if value <= 0:
            self.currCapacity, self.initialCapacity = 1, 1
        else:
            self.currCapacity, self.initialCapacity = value, value

    # Destructor
    def __del__(self):
        print("Destructor Called")
        return

    # Copy Constructor - creates a new instance of queue
    def __copy__(self):
        copy = Dynamic_queue(self.currCapacity)
        if len(self.elements) == 0:
            return copy
        else:
            for x in self.elements:
                copy.elements.append(x)
        return copy

    # Accessors - access the queue, but doesn't modify it
    # Returns the object at the head of the queue
    def head(self):
        if len(self.elements) == 0:
            return "empty"
        else:
            return self.elements[0]

    # Returns the number of objects currently stored in the queue
    def size(self):
        """
        Should iterate through elements list and count each element
        and return count. Ex: If list is size 10 and holds 2 elements,
        then it will return wrong count of 10 elements.
        """
        return len(self.elements)

    # Returns true if the queue is empty. Returns false otherwise
    def empty(self):
        """
        Should iterate through elements list and count each element
        and return count. Ex: If list is size 10 and holds 2 elements,
        then it will return wrong count of 10 elements.
        """
        if len(self.elements) == 0:
            return True
        else:
            return False

    # Returns the current capacity of the queue.
    def capacity(self):
        return self.currCapacity

    # Mutators - Changes values in the queue
    # will swap all the member variables of this queue with those of the argument
    def swap(self, swapper):
        for x in self.elements:
            self.elements.pop(0)
            self.elements.append(swapper)
        return self.elements

    # Swaps member variables with the copy on the right side of the operator
    def __eq__(self, copy):
        # Swaps lists
        temp = copy.elements, self.elements
        self.elements = temp[0]
        copy.elements = temp[1]
        # Swaps other member variables
        temp1, temp2 = self.currCapacity, self.initialCapacity
        self.currCapacity, self.initialCapacity = copy.currCapacity, copy.initialCapacity
        copy.currCapacity, copy.initialCapacity = temp1, temp2
        return copy, temp

    # Insert the argument at the end of the queue.
    # If the array is full before the argument is placed, the array is doubled first.
    """
    Should double the elements list if it is full when enqueuing additional element
    """
    def enqueue(self, value):
        if self.currCapacity == self.size():
            self.currCapacity *= 2
        self.elements.append(value)
        return

    # Removes the object at the front of the queue. If, after the object is removed, the array is
    # 1/4 full, and its greater than the initial capacity, the capacity is halved.
    """
    Should half the elements list if it is 0.25% full when dequeuing from list
    """
    def dequeue(self):
        self.elements.pop(0)
        if self.size == 0:
            return
        elif (self.capacity() > self.initialCapacity) & (self.size()/self.capacity() <= 0.25):
            self.currCapacity /= 2
            self.currCapacity = int(self.currCapacity)
        return

    # Resets member variables to empty queue. The array is resized to the initial capacity
    def clear(self):
        """
        Should clear list and then create new list with initial capacity as its size.
        """
        self.elements.clear()
        return self.elements
