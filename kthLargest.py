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

def populate(root,k,cnt):
    if(root == None):
        return -1;
    res = populate(root.right, k, cnt)
    if(res == -1):    
        cnt[0] -= 1
        if(cnt[0] == 0):
            return root.data
        return populate(root.left, k ,cnt)
    return res
    

def kthLargest(root, k):
    return populate(root,k,[k])

def main(data, k):
    root = None
    for i in data.split():
        root = insert(root, i)
    inorder(root)
    print()
    preorder(root)
    print()
    print(kthLargest(root,k))  

main("1 2 3 4 5 6", 1)

main("1 2 3 4 5 6", 3)

main("1 2 3 4 5 6", 5)

main("1 2 3 4 5 6", 1)