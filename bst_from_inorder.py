class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

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

def postorder(root):
    if(root == None):
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=" ")

def construct(data,MIN,MAX):
    if(len(data) > 0):
        d=data[0]
        if(d > MIN and d < MAX):
            root=Node(data.pop(0))
            root.left=construct(data,MIN,root.data)
            root.right=construct(data,root.data,MAX)
            return root
    return None


def construct_bst(root,key):
    if(root  == None):
        return Node(key)
    if(root.data < key):
        root.right=construct_bst(root.right,key)
    else:
        root.left=construct_bst(root.left,key)
    return root

def main(data):
    root=None
    for i in data:
        root=construct_bst(root,i)
    preorder(root)
    print()
    print(data)

    root=construct(data,float('-inf'),float('inf'))
    preorder(root)
    print()
    print(data)


main([10, 5, 1, 7, 40, 50])