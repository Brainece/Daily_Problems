class Node:
    """ Implementation of binary tree, in which each node can have a maximum of two children
    """
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_recursive(self.root,data)
    
    def _insert_recursive(self, node, value):
        if value < node.data:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left,value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right,value)
        

    def printInOrder(self, node):
        if node is not None:
            self.printInOrder(node.left)
            print(node.data, end=" ")
            self.printInOrder(node.right)


if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(50)
    tree.insert(30)
    tree.insert(20)
    tree.insert(40)
    tree.insert(70)
    tree.insert(60)
    tree.insert(80)

    print("Inorder Traversal")
    tree.printInOrder(tree.root)
    

