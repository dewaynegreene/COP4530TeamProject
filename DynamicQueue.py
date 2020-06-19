#Authors: Andres Greene
#         Raquel Garcia
#         Laureano Griffin
#         Josue Gonzalez-Picasso

class Dynamic_queue:

    #Member variables initialized here



    #Constructor
    #This initializes the queue. The user inputs the size of the array.
    #If the user inputs 0 or a negative integer, set n = 1
    #The default initial capacity is n = 10

    def __init__(self, value):
        self.elements = []

    #Destructor

    def __del__(self):

    #Copy Constructor
    #This should create a new instance of the queue

    def __copy__(self):

    #Accessors
    #These functions access the queue. They do not modify it

    def head(self):
        # Returns the object at the head of the queue

    def size(self):
        # Returns the number of objects currently stored in the queue

    def empty(self):
        # Returns true if the queue is empty. Returns false otherwise

    def capacity(self):
        # Returns the current capacity of the queue.

    #Mutators
    #These functions change the values in the queue

    def swap(self):
        #will swap all the member variables of this queue with those of the argument

    def operator(self):
        #?????

    def enqueue(self, value):
        # Insert the argument at the end of the queue. If the array is full before the argument is placed,
        # the array is doubled first.

    def dequeue(self, value):
        # Removes the object at the front of the queue. If, after the object is removed, the array is
        # 1/4 full, and its greater than the initial capacity, the capacity is halved.

    def clear(self):
        #Empties the queue. The array is resized to the initial capacity