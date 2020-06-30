# Authors: Andres Greene
#         Raquel Garcia
#         Laureano Griffin
#         Josue Gonzalez-Picasso

from DynamicQueue import Dynamic_queue

# File is used to test the dynamic queue class

# Tests the constructor
print("CONSTRUCTOR")
testSize = input("Enter the size of the queue: ")
if testSize == '':
    testQueue = Dynamic_queue()
else:
    testSize = int(testSize)
    testQueue = Dynamic_queue(testSize)

print("The initial capacity is " + str(testQueue.initialCapacity))
print("The current capacity is " + str(testQueue.currCapacity))
testQueue.elements.append(5);
testQueue.elements.append(10);

# Tests the copy constructor
print("\nCOPY CONSTRUCTOR")
copy = testQueue.__copy__()
print("The copy's initial capacity is " + str(copy.initialCapacity))
print("The copy's current capacity is " + str(copy.currCapacity))
print("The Original List: " + str(testQueue.elements))
print("The Copied List: " + str(copy.elements))

# Tests the Accessors
print("\nACCESSORS")
print("What is stored at the head is " + str(testQueue.head()))
print("The number of elements currently stored is " + str(testQueue.size()))
print("Is the queue empty? " + str(testQueue.empty()))
print("The capacity of the queue is " + str(testQueue.capacity()))

# Tests the Mutators
print("\nMUTATORS")
print("SWAP")

print("\nEQUAL OPERATOR")
copy.enqueue(6)
print("The Original List: " + str(testQueue.elements))
print("The initial capacity is " + str(testQueue.initialCapacity))
print("The current capacity is " + str(testQueue.currCapacity))
print("The Copied List: " + str(copy.elements))
print("The copy's initial capacity is " + str(copy.initialCapacity))
print("The copy's current capacity is " + str(copy.currCapacity))
testQueue == copy
print("Swapped\nThe Original List: " + str(testQueue.elements))
print("The initial capacity is " + str(testQueue.initialCapacity))
print("The current capacity is " + str(testQueue.currCapacity))
print("The Copied List: " + str(copy.elements))
print("The copy's initial capacity is " + str(copy.initialCapacity))
print("The copy's current capacity is " + str(copy.currCapacity))

print("\nENQUEUE")
print("testQueue's elements:" + str(testQueue.elements))
print("The initial capacity is " + str(testQueue.initialCapacity))
print("The current capacity is " + str(testQueue.currCapacity))
testQueue.enqueue(5)
print("After dequeue, testQueue's elements:" + str(testQueue.elements))
print("The current capacity is " + str(testQueue.currCapacity))

print("\nDEQUEUE ")
print("testQueue's elements:" + str(testQueue.elements))
print("The initial capacity is " + str(testQueue.initialCapacity))
print("The current capacity is " + str(testQueue.currCapacity))
testQueue.dequeue()
print("After dequeue1, testQueue's elements:" + str(testQueue.elements))
print("The current capacity is " + str(testQueue.currCapacity))

testQueue.dequeue()
print("After dequeue2, testQueue's elements:" + str(testQueue.elements))
print("The current capacity is " + str(testQueue.currCapacity))


print("\nCLEAR")

# Starts to create actual main
# Needs to demonstrate things cna be removed from queue, added to queue, and the size & capacity will dynamically change


# Tests the destructor
# Destructor is called at the end of the program
print("\nDestructor")




