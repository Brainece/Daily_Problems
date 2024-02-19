class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inOrder(root):
    """Implementation of inorder traversal which first visits nodes in the left subtree, then the root node,
    and finally visits all the nodes in the right subtree
    """
    if root:
        # traverse left
        inOrder(root.left)
        print(str(root.data) + "->", end="")
        inOrder(root.right)

def preOrder(root):
    """ Implementation of preorder traversal which first begins by visiting the root node, followed by the left
    subtree and then finally visits the right subtree
    """
    if root:
        # traverse root
        print(str(root.data) + "->", end="")
        # traverse left
        preOrder(root.left)
        # traverse right
        preOrder(root.right)

def postOrder(root):
    """ in this case the left subtree is visited, followed by the right subtree and then finally the root is visited
    """
    if root:
        # traverse left
        postOrder(root.left)
        # traverse right
        postOrder(root.right)
        # travesre root
        print(str(root.data) + "->", end="")


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)

    print("Inorder Traversal")
    inOrder(root)

    print("\nPreorder Traversal")
    preOrder(root)

    print("\nPostorder Traversal")
    postOrder(root)

    print("")




