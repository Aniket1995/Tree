import math

class Node:
    def __init__(self,data):
        self.data=int(data)
        self.left=None
        self.right=None

def get_inorder(root, res):
    if(root == None):
        return 
    get_inorder(root.left, res)
    res.append(root)
    get_inorder(root.right, res)

def findPreSuc(root, pre, suc, key):
    in_order=[]
    get_inorder(root, in_order)
    if(in_order[0].data > key):
        suc[0]=in_order[0]
    elif(in_order[-1].data < key):
        pre[0]=in_order[-1]
    else:
        i=0
        while(i < len(in_order) and in_order[i].data < key):
            i+=1
        if(in_order[i].data == key):
            if(i-1 >= 0):
                pre[0]=in_order[i-1]
            if(i+1 < len(in_order)):
                suc[0]=in_order[i+1]
        else:
            if(i-1 >= 0):
                pre[0]=in_order[i-1]
            suc[0]=in_order[i]


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
    pre=[None]
    suc=[None]
    findPreSuc(root, k, pre, suc)
    print(pre[0])
    print(suc[0])

main("1 2 3 4 5 6", 1)

main("1 2 3 4 5 6", 3)

main("1 2 3 4 5 6", 5)

main("1 2 3 4 5 6", 1)