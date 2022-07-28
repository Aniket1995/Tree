
class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None


#contrust tree where root is max then all children

def construct(data):
    if(len(data) == 0):
        return None

    max_elem=max(data)
    max_index=data.index(max_elem)
    left=data[:max_index]
    right=data[max_index+1:]
    root=Node(max_elem)
    root.left=construct(left)
    root.right=construct(right)
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

def main(data):
    root=construct(data)
    inorder(root)
    print()
    preorder(root)

main([1, 5, 10, 40, 30, 15, 28, 20])

