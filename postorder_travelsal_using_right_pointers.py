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

def print_right(root):
    if(root is None):
        return 
    print(root.data,end=" ")
    print_right(root.right)

def get_rightmost(left):
    if(left is None):
        return 
    c=left
    while(c.right):
        c=c.right
    return c

def reorder(root):
    if(root == None):
        return
    reorder(root.left)
    reorder(root.right)
    left_rightmost=get_rightmost(root.left)
    if(left_rightmost != None):
        left_rightmost.right=root.right
    root.right=root.left

def main():
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    root.right.left=Node(6)
    root.right.right=Node(7)
    # inorder(root)
    # print()
    preorder(root)
    reorder(root)
    print()
    print_right(root)
    # print()
    # postorder(root)

main()