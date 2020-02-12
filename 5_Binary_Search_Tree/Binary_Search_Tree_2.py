


class Node(object):
    def __init__(self, value):
        self.count = 0
        self.value = value
        self.right = None
        self.left  = None


class Binary_Search_Tree(object):

    def __init__(self):
        self.root = None


    def insert(self, val):
        node = Node(val)
        if not self.root:
            self.root = node
        else:
            current_node = self.root
            while True:
                if node.value == current_node.value:
                    current_node.count += 1
                    return
                if node.value  < current_node.value and not current_node.left:
                    current_node.left = node
                    print("Added a left node: " + str(node.value))
                    return
                elif node.value < current_node.value and current_node.left:
                    current_node = current_node.left
                elif node.value > current_node.value and not current_node.right:
                    current_node.right = node
                    print("Added a right node: " + str(node.value))
                    return
                elif node.value > current_node.value and current_node.right:
                    current_node = current_node.right
                else:
                    print("AHHHHHHHHHHHHHHHH I didn't include the case for" + str(node.value))
                    return


    def print_pre_order_traversal(self):
        if not self.root:
            print("The Tree is empty")
            return
        node_stack = []
        node_stack.append(self.root)

        while (len(node_stack) > 0):
            node = node_stack.pop()
            print(node.value)

            if node.right:
                node_stack.append(node.right)
            if node.left:
                node_stack.append(node.left)
        
    def print_post_order_traversal(self):
        if not self.root:
            print("The Tree is empty")
            return
        
        node_stack = []
        node_stack.append(self.root)
        current_node = self.root
        prev_node = None

        while(len(node_stack) > 0):
            if current_node.left

        





        return        



    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        return False

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        return ""

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        return False

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        return traversal




tree = Binary_Search_Tree()
tree.insert(15)
tree.insert(10)
tree.insert(20)
tree.insert(7)
tree.insert(11)
tree.insert(18)
tree.insert(23)
tree.print_pre_order_traversal()