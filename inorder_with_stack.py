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

def inorder_with_stack(root):
    if(root == None):
        return []
    res=[]
    s=[]
    c=root
    while(True):
        if(c != None):
            s.append(c)
            c=c.left 
        elif(len(s) > 0):
            c=s.pop()
            res.append(c.data) #print
            c=c.right
        else:
            break
    return res

def preorder_with_stack(root):
    if(root == None):
        return []
    res=[]
    s=[]
    while(True):
        if(root!=None):
            res.append(root.data) #print
            if(root.right):
                s.append(root.right)
            root=root.left
        elif(len(s) > 0):
            root=s.pop()
        else:
            break
    return res


def postorder_without_stack(root):
    if(root == None):
        return []
    res=[]
    c=root
    while(c and c.data not in res):
        if(c.left and c.left.data not in res):
            c=c.left
        elif(c.right and c.right.data not in res):
            c=c.right
        else:
            res.append(c.data)
            c=root
    return res


def main():
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    root.right.left=Node(6)
    root.right.right=Node(7)
    inorder(root)
    print()
    res=inorder_with_stack(root)
    print("\n"+str(res))
    print()
    
    postorder(root)
    print()
    res=postorder_without_stack(root)
    print("\n"+str(res))
    print()

    preorder(root)
    print()
    res=preorder_with_stack(root)
    print("\n"+str(res))
    print()

main()