# Authors: Andres Greene
#         Raquel Garcia
#         Laureano Griffin
#         Josue Gonzalez-Picasso

from DynamicQueue import Dynamic_queue

# File is used to test the dynamic queue class

# Tests the constructor
print("Constructor")
testSize = input("Enter the size of the queue: ")
if testSize == '':
    testQueue = Dynamic_queue()
else:
    testSize = int(testSize)
    testQueue = Dynamic_queue(testSize)
print("The initial capacity is " + str(testQueue.initialCapacity))
print("The current capacity is " + str(testQueue.currCapacity))

# Tests the destructor
print("\nDestructor")

# Tests the copy constructor
print("\nCopy Constructor")


# Tests the Accessors
print("\nAccessors")
print("What is stored at the head is " + str(testQueue.head()))
print("The number of elements currently stored is " + str(testQueue.size()))
print("Is the queue empty? " + str(testQueue.empty()))
print("The capacity of the queue is " + str(testQueue.capacity()))

# Tests the Mutators
print("\nMutators")
print("The swap function")
print("The equal function ")
print("The enqueue function")
print("The dequeue function ")
print("The clear function")




