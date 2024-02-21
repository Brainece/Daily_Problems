"""
A binary search tree is a type of binary tree in which the parent node value is greater than the node values in its 
left subtree and less than all the node values in its right subtree. Additionally there can't be repeat nodes.
"""
import graphviz
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def addChild(self,data):
        if data == self.data:
            return # node already exists
        if data < self.data:
            if self.left:
                self.left.addChild(data)
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.addChild(data)
            else:
                self.right = Node(data)
        
    def search(self, data):
        if data == self.data:
            print(self.data)
            return True
        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                print("Not Found")
                return False
        else:
            if self.right:
                return self.right.search(data)
            else:
                print("Not Found")
                return False

    def inOrderTraversal(self):
        if self.left:
            self.left.inOrderTraversal()
        print(self.data, end=" ")
        if self.right:
            self.right.inOrderTraversal()

    def vizBSTree(self):
        dot = graphviz.Digraph()
        dot.node(str(self.data))

        def add_nodes_edges(node):
            if node.left:
                dot.node(str(node.left.data))
                dot.edge(str(node.data),str(node.left.data))
                add_nodes_edges(node.left)
            if node.right:
                dot.node(str(node.right.data))
                dot.edge(str(node.data),str(node.right.data))
                add_nodes_edges(node.right)
        add_nodes_edges(self)
        dot.render('binary_tree', view=True, format='png')

if __name__ == "__main__":
    root = Node(10)
    root.addChild(6)
    root.addChild(5)
    root.addChild(8)
    root.addChild(13)
    root.addChild(15)
    root.addChild(12)
    root.inOrderTraversal()

    print()
    root.search(7)
    root.vizBSTree()