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

def countNode(root):
    if(root == None):
        return 0
    return 1 + countNode(root.left) + countNode(root.right)
    
def construct(data):
    if(len(data) == 0):
        return None
    
    root=Node(data.pop(0))
    q=[root]

    while(len(q) > 0):
        n=q.pop(0)
        if(n.left == None and len(data) > 0):
            if(data[0] != -1):
                n.left=Node(data.pop(0))
                q.append(n.left)
            else:
                data.pop(0)
        if(n.right == None and len(data) > 0):
            if(data[0] != -1):
                n.right=Node(data.pop(0))
                q.append(n.right)
            else:
                data.pop(0)

    return root

def checkIt(root,total):
    if(root == None):
        return False
    c=countNode(root)
    if(c == total - c):
        return True
    return checkIt(root.left,total) or checkIt(root.right,total)

def main(data):
    l=len(data)
    root=construct(data)
    inorder(root)   
    print()
    print(countNode(root))
    print(l)
    print(checkIt(root,countNode(root)))

main([1,2,3,4,5,6,7,9])