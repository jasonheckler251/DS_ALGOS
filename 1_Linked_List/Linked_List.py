##PROS

## Linked lists are dynamic data structures
## Can allocate the needed memory in run-time
## Very efficient if we want to manipulate the first element
## Can store items of different sizes. An array assumes same size elements.


##CONS

## Wastes memory because each node refereneces another node.
## Nodes must be read from the beginning of the list. Arrays are accessed via index.
## Singly linked lists are difficult to navigate backward.


class Node(object):

    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def insertStart(self, data):
        self.size = self.size +1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    #O(N)
    def remove(self, data):
        
        if self.head is None:
            return
        
        self.size = self.size -1

        currentNode = self.head
        previousNode = None

        while currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.nextNode
        
        if previousNode is None:
            self.head = currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode



    # O(1)
    def getSize(self):
        return self.size

    #O(N)
    def calcSize(self):
        actualNode = self.head
        size = 0

        while actualNode is not None:
            size+=1
            actualNode = actualNode.nextNode

        return size
    
    #O(N)
    def insertEnd(self, data):

        self.size = self.size + 1
        newNode = Node(data)
        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode

    #O(N)
    def traverseList(self):

        actualNode = self.head
        while actualNode is not None:
            print("%d " % actualNode.data)
            actualNode = actualNode.nextNode
