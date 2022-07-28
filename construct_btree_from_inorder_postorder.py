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

def construct(root,in_order,post_order):
    if(len(in_order) == 0 or len(post_order) == 0):
        return
    if(root == None):
        root=Node(post_order.pop())
    if(root and root.data in in_order and len(post_order) > 0):
        in_index=in_order.index(root.data)
        left_in_order=in_order[:in_index]
        right_in_order=in_order[in_index+1:]
        if(len(right_in_order) > 0):
            root.right=construct(root.right,right_in_order,post_order)
        if(len(left_in_order) > 0):
            root.left=construct(root.left,left_in_order,post_order)
    return root

def main(in_order,post_order):
    root=construct(None,in_order,post_order)
    inorder(root)
    print()
    preorder(root)

main(["B","A","C"],["B","C","A"])