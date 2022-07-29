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

def construct(data):
    if(len(data) == 0):
        return None
    root=Node(data[0])
    q=[root]
    i=1
    l=len(data)
    while(i < l and len(q) > 0):
        n=q.pop(0)
        if(n.left == None):
            n.left = Node(data[i])
            i+=1
            q.append(n.left)
        if(n.right == None):
            n.right = Node(data[i])
            i+=1
            q.append(n.right)
    return root

def main(data):
    root=construct(data)
    inorder(root)

main([1,2,3])