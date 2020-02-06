



class Node(object):
    
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertNode(data, self.root)    

    # O(logn) if the tree is balanced
    def insertNode(self, data, node):
        ## node will be inserted on left side of the root
        if data < node.data:
            ##if a left child exists, call this function recursively, where the left child is the root node
            if node.leftChild:
                self.insertNode(data, node.leftChild)
            else:
                node.leftChild = Node(data)
        ## node will be inserted on the right side of the root
        else:
            ##if a right child exists, call this function recursively, where the right child is the root node
            if node.rightChild:
                self.insertNode(data, node.rightChild)
            else:
                node.rightChild = Node(data)


    def getMinValue(self):
        if self.root:
            return self.getMin(self.root)


    def getMaxValue(self):
        if self.root:
            return self.getMin(self.root)
    
    def getMin(self, node):
        if node.leftChild:
            return self.getMin(node.leftChild)
        else:
            return node.data

    def getMax(self, node):
        if node.rightChild:
            return self.getMax(node.rightChild)
        else:
            return node.data

    
    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)



    def traverseInOrder(self, node):

        if node.leftChild:
            self.traverseInOrder(node.leftChild)
        
        print("%s " % node.data)

        if node.rightChild:
            self.traverseInOrder(node.rightChild)

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
                print("Remvoing a leaf node")
                del node
                return None
            if not node.leftChild:
                print("Removing a node with a single right child...")
                tempNode = node.rightChild
                del node
                return tempNode
            elif not self.rightChild:
                print("Removing a node with a single left child...")
                tempNode = node.leftChild
                del node
                return tempNode

            print("Removing node with two children")
            tempNode = self.getPredecessor(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.removeNode(tempNode.data, node.leftChild)
            

def getPredecessor(self, node):
    if node.rightChild:
        return self.getPredecessor(node.right)
    else:
        return node




