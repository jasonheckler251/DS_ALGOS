

class Node(object):
    def __init__(self,data):
        self.data = data
        self.height = 0
        self.leftChild = None
        self.rightChild = None



class AVL(object):
    def __init__(self):
        self.root = None


    def insert(self, data):
        self.root = self.insertNode(data, self.root)

    def insertNode(self, data, node):
        if not node:
            return Node(data)
        if data < node.data:
            node.leftChild = self.insertNode(data, node.leftChild)
        else:
            node.rightChild = self.insertNode(data, node.rightChild)    

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1

        return self.settleViolation(data, node)

    def remove(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root)

    def removeNode(self, data, node):

        if not node:
            return node
        
        if data < node.data:
            node.leftChild = self.removeNode(data, node.leftChild)
        elif data > node.data:
            node.rightChild = self.removeNode(data, node.rightChild)
        else:
            if not node.leftChild and not node.rightChild:
                print("Removing a leaf node...")
                del node
                return None
            
            if not node.leftChild:
                print("Removing right child...")
                tempNode = node.rightChild
                del node
                return tempNode

            elif not node.rightChild:
                print("Removing left child...")
                tempNode = node.leftChild
                del node
                return tempNode

            print("Removing node with two children")
            tempNode = self.getPredecessor(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.removeNode(tempNode.data, node.leftChild)


        if not node:
            return node

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1

        balance = self.calcBalance(node)

        if balance > 1 and self.calcBalance(node.leftChild) >= 0:
            print("Left Left Heavy situation...":)
            return self.rotateRight(node)

        if balance < -1 and self.calcBalance(node.leftChild) < 0:
            print("Right Right Heavy situation..")
            return self.rotateLeft(node)
        
        if balance > 1 and self.calcBalance(node.rightChild) <= 0:
            print("Left Right heavy situation..")
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)

        if balance < -1 and self.calcBalance(node.rightChild) > 0:
            print("Right Left heavy situation..")
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)

        return node

    def settleViolation(self, data, node):
        balance = self.calcHeight(node)

        #case1 -> Left Heavy Situation
        if balance > 1 and data < node.leftChild.data:
            print("Left Left Heavy situation...":)
            return self.rotateRight(node)

        if balance < -1 and data > node.rightChild.data:
            print("Right Right Heavy situation..")
            return self.rotateLeft(node)
        
        if balance > 1 and data > node.leftChild.data:
            print("Left Right heavy situation..")
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)

        if balance < -1 and data < node.rightChild.data:
            print("Right Left heavy situation..")
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)

        return node

    def calcHeight(self, node):
        if not node:
            return -1
        else:
            return node.height

    # if it returns value > 1, then this is left heavy tree...so we need a right rotation
    # if it returns value < -1 then this is a right heavy tree...so we need a left rotation
    def calcBalance(self, node):
        if not node:
            return 0
        return self.calcHeight(node.leftChild) - self.calcHeight(node.rightChild)

    def traverse(self):
        if self.root:
            self.traverseInorder(self.root)

    def traverseInorder(self, node):
        if node.leftChild:
            self.traverseInorder(node.leftChild)
        
        print("%s " % node.data)

        if node.rightChild:
            self.traverseInorder(node.rightChild)


    def rotateRight(self, node):

        print("Rotating to the right on node ", node.data)

        tempLeftChild = node.leftChild
        t = tempLeftChild.rightChild

        tempLeftChild.rightChild = node
        node.leftChild = t
        
        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1
        tempLeftChild.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1

        return tempLeftChild


    def rotateLeft(self, node):

        print("Rotating to the right on node ", node.data)

        tempRightChild = node.rightChild
        t = tempRightChild.leftChild

        tempRightChild.leftChild = node
        node.rightChild = t
        
        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1
        tempRightChild.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1

        return tempRightChild        