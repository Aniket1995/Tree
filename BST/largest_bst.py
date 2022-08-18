import math

class Node:
    def __init__(self,data):
        self.data=int(data)
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

def construct(data):
    if(len(data) == 0):
        return None
    
    root=Node(data.pop(0))
    q=[root]

    while(len(q) > 0):
        n=q.pop(0)
        if(n.left == None and len(data) > 0):
            if(data[0] != 'N'):
                n.left=Node(data.pop(0))
                q.append(n.left)
            else:
                data.pop(0)
        if(n.right == None and len(data) > 0):
            if(data[0] != 'N'):
                n.right=Node(data.pop(0))
                q.append(n.right)
            else:
                data.pop(0)

    return root

def bstSize(root, min_, max_):
    if(root == None):
        return 0
    if(root.left and root.left.data >= root.data):
        return 0
    if(root.right and root.right.data <= root.data):
        return 0
    if(root.data <= min_ or root.data >= max_):
        return 0
    l = bstSize(root.left, min_, root.data)
    if(root.left and l == 0):
        return 0
    r = bstSize(root.right, root.data, max_)
    if(root.right and r == 0):
        return 0
    return 1 + l + r 

def largestBstUtil(root, max):
    if(root == None):
        return
    size = bstSize(root, -math.inf, math.inf)
    if(max[0] < size):
        max[0] = size
    largestBstUtil(root.left, max)
    largestBstUtil(root.right, max)

def largestBST(root):
    if(root == None):
        return 0
    max=[0]
    largestBstUtil(root, max)
    return max[0]
    

def main(data):
    # for i in map(int, data.split()):
    #     root = insert(root, i)
    root = construct(data.split())
    inorder(root)
    print()
    preorder(root)
    print() 
    print(largestBST(root))

# main("1 2 3 4 5 6")

# main("6 N 3 N 6 N 5 N 3 N 1 N 3 N 8 N 7 N 5")

main("8 11 1 10 N 1 6 9 4")

# main("1 2 3 4 5 6", 3)

# main("1 2 3 4 5 6", 5)

# main("1 2 3 4 5 6", 1)