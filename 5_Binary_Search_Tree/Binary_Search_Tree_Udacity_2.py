class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)





    def insert(self, new_val):
        if not self.root:
            self.root = Node(new_val)
        else:
            return self.insert_helper(new_val, self.root)

    def insert_helper(self, new_val, node):
        if new_val < self.root.value:
            if node.left:
                self.insert_helper(new_val, node.left)
            else:
                node.left = Node(new_val)
        elif new_val > self.root.value:
            if node.right:
                self.insert_helper(new_val, node.right)
            else:
                node.right = Node(new_val)


    def search(self, find_val):
        if self.root is None:
            return False
        else:
            return self.preorder_search(self.root, find_val)


    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        if start:
            if start.value == find_val:
                return True
            else:
                return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)
        return False

    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print (tree.search(4))
# Should be False
print (tree.search(6))