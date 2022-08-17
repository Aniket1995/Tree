class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

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

def isLeaf(root):
    return root != None and root.left == None and root.right == None

def rightMost(root):
    if(root == None):
        return root
    while(root.right):
        root=root.right
    return root

def leftMost(root):
    if(root == None):
        return root
    while(root.left):
        root=root.left
    return root
        
def deleteNode(root, X):
    if(root == None):
        return root
    if(root.data == X):
        if(isLeaf(root)):
            return None
        elif(root.right):
            root.data = leftMost(root.right).data
            root.right = deleteNode(root.right, root.data)
        elif(root.left):
            root.data = rightMost(root.left).data
            root.left = deleteNode(root.left, root.data)
        return root
            
    if(root.data < X):
        root.right = deleteNode(root.right, X)
    else:
        root.left = deleteNode(root.left, X)
    return root

def main(data):
    root = None
    for i in data:
        root = insert(root, i)
    inorder(root)
    print()
    preorder(root)
    print()

main("1 2 3 4 5 6")

    