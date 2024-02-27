""" Implementation of AVL Tree which is a self-balancing BST that contains an extra attribute called a balancing
factor. Accepted values for BF are {-1, 0, 1}. If the values are exceeded then rotations must be done to correct
the tree. BF = {Height of LSubtree - Height of RSubtree }
"""
import sys
#import graphviz

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
                #return self.rightRotate(root)
                return self.LLRotate(root)
            else:
                #root.left = self.leftRotate(root.left)
                return self.LRRotate(root)
                #return self.rightRotate(root)
        
        if balanceFactor < -1:
            if data > root.right.data:
                #return self.leftRotate(root)
                return self.RRRotate(root)
            else:
                #root.right = self.rightRotate(root.right)
                #return self.leftRotate(root)
                return self.RLRotate(root)
        
        return root
    
    def LLRotate(self,node):
        y = node.left
        node.left = y.right
        y.right = node

        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y
    
    def RRRotate(self,node):
        y = node.right
        node.right = y.left
        y.left = node

        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y
    
    def LRRotate(self,node):
        y = node.left.right
        t3 = node.left
        t3.right = y.left
        y.left = t3
        node.left = y.right
        y.right = node

        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def RLRotate(self,node):
        y = node.right.left
        t2 = node.right
        t2.left = y.right
        node.right = y.left
        y.left = node
        y.right = t2

        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y
    
    """
    def leftRotate(self,z):
        y = z.right
        t2 = y.left
        y.left = z
        z.right = t2
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y
    
    def rightRotate(self,z):
        y = z.left
        t3 = y.right
        y.right = z
        z.left = t3
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        z.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

    """


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
    nums = [33,13,52,9,21,61,8,11,5,2,15]
    for num in nums:
        root = myTree.insertNode(root, num)
    
    myTree.printHelper(root," ",True )
    
            
            