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
    while(testSize.isalpha() or int(testSize) < 0 ):
        testSize = input("Invalid input. Please re-enter size of queue: ")
    testSize = int(testSize)
    testQueue = Dynamic_queue(testSize)


print("The initial capacity is " + str(testQueue.initialCapacity))
print("The current capacity is " + str(testQueue.currCapacity))

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
print("The Original List: " + str(testQueue.elements))
doSwap = input("Swap all member variables of this queue? (Y/N): ")
while(doSwap != "Y" and doSwap != "y" and doSwap != "n" and doSwap != "N"):
        doSwap = input("Invalid input. Please re-enter (Y/N): ")
if doSwap == "Y" or doSwap == "y" or doSwap == "n" or doSwap == "N":
    if(doSwap == "Y" or doSwap == "y"):
        newVar = input("Enter new variable to replace all variables with: ")
        newVar = int(newVar)
        print("New queue after swap: " + str(testQueue.swap(newVar)))




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
i = 0
while i < 5:
    print("testQueue's elements:" + str(testQueue.elements))
    print("The initial capacity is " + str(testQueue.initialCapacity))
    print("The current capacity is " + str(testQueue.currCapacity))
    testQueue.enqueue(5)
    print("After enqueue, testQueue's elements:" + str(testQueue.elements))
    print("The current capacity is " + str(testQueue.currCapacity) + "\n")
    i += 1

print("\nDEQUEUE ")
i = 0
while i < 4:
    print("testQueue's elements:" + str(testQueue.elements))
    print("The initial capacity is " + str(testQueue.initialCapacity))
    print("The current capacity is " + str(testQueue.currCapacity))
    testQueue.dequeue()
    print("After dequeue, testQueue's elements:" + str(testQueue.elements))
    print("The current capacity is " + str(testQueue.currCapacity) + "\n")
    i +=1

testQueue.dequeue()
print("After dequeue, testQueue's elements:" + str(testQueue.elements))
print("The current capacity is " + str(testQueue.currCapacity))

# ADDING/DELETING TO OR FROM QUEUE
print("\nADDING/DELETING VAR TO QUEUE")
userAdd = input("Add or delete variable to Queue? (Y/N): ")
while(userAdd != "Y" and userAdd != "y" and userAdd != "n" and userAdd != "N"):
        userAdd = input("Invalid input. Please re-enter (Y/N): ")
if userAdd == "Y" or userAdd == "y":
    userChoice = input("Enter 'A' for adding or 'D' for deleting a variable (A/D): " )
    while (userChoice != "A" and userChoice != "a" and userChoice != "D" and userChoice != "d"):
        userChoice = input("Invalid input. Please re-enter 'A' for adding or 'D' for deleting a variable: ")
    if userChoice == "A" or userChoice == "a":
        # Adding preset value to the queue 3
        testQueue.enqueue(3)
        print("Variable 3 added to queue.")
        print("Updated queue: ", testQueue.elements)
    elif userChoice == "D" or userChoice == "d":
        # Dequeuing from front
        testQueue.dequeue()
        print("Front element deleted from queue.")
        print("Updated queue: ", testQueue.elements)


print("\nCLEAR")
print("Clearing testQueue's elements: " + str(testQueue.clear()))
print("The initial capacity is " + str(testQueue.initialCapacity))
print("The current capacity is " + str(testQueue.currCapacity))

# Tests the destructor
# Destructor is called at the end of the program
print("\nDestructor")





