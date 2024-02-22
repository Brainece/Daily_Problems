""" Implementation of AVL Tree which is a self-balancing BST that contains an extra attribute called a balancing
factor. Accepted values for BF are {-1, 0, 1}. If the values are exceeded then rotations must be done to correct
the tree. BF = {Height of LSubtree - Height of RSubtree }
"""
import sys
import graphviz

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insertNode(self, root, data):
        if not root:
            return TreeNode(data)
        elif data < root.data:
            root.left = self.insertNode(root.left, data)
        else:
            root.right = self.insertNode(root.right, data)
        
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balanceFactor = self.getBalanceFactor(root)

        if balanceFactor > 1:
            if data < root.left.data:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        
        if balanceFactor < -1:
            if data > root.right.data:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        
        return root
    
    def getHeight(self, root):
        if not root:
            return 0
        return root.height
    
    def getBalanceFactor(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)
    
    def preOrderTraversal(self, root):
        if not root:
            return
        print("{0}".format(root.key), end=" ")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def printHelper(self, currPtr, indent, last):
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += " "
            else:
                sys.stdout.write("L-----")
                indent += "| "
            print(currPtr.data)
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, False)
        
    def vizTree(self):
        pass

if __name__ == "__main__":
    myTree = AVLTree()
    root = None
    nums = [33,13,52,9,21,61,8,11]
    for num in nums:
        root = myTree.insertNode(root, num)
    
    myTree.printHelper(root," ",True )
    
            
            