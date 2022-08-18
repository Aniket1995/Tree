import math

class Node:
    def __init__(self,data):
        self.data=int(data)
        self.left=None
        self.right=None

def is_bst(root,min_,max_):
    if(root == None):
        return True
    if(min_ > root.data or root.data > max_):
        return False
    if(root.left and root.data < root.left.data):
        return False
    if(root.right and root.data > root.right.data):
        return False
    return is_bst(root.left, min_, root.data) and is_bst(root.right, root.data, max_)

def isBST(root):
    if(root == None):
        return True
    return is_bst(root,-math.inf,math.inf)

def insert(root, key):
    if(root == None):
        return Node(key)
    if(root.data < key):
        root.right = insert(root.right, key)
    if(root.data > key):
        root.left = insert(root.left, key)
    return root

def inorder(root):
    if(root == None):
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)

def preorder(root):
    if(root == None):
        return 
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)
    

def main(data, k):
    root = None
    for i in map(int, data.split()):
        root = insert(root, i)
    inorder(root)
    print()
    print(isBST(root))

main("1 2 3 4 5 6", 1)

main("1 2 3 4 5 6", 3)

main("1 2 3 4 5 6", 5)

main("1 2 3 4 5 6", 1)