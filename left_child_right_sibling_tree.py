class Node:
    def __init__(self,data):
        self.data=str(data)
        self.left=None
        self.middle=None
        self.right=None

def construct(root):
    if(root == None):
        return None
    left=construct(root.left)
    mid=construct(root.middle)
    right=construct(root.right)
    if(left and mid and right):
        left.right=mid
        mid.right=right
        root.middle=None
        root.right=None
    return root

def print_(root):
    if(root == None):
        return
    res=[]
    c=root
    while(c):
        p=c
        q=[]
        while(p):
            q.append(p.data)
            p=p.right
        res.append("->".join(q))
        c=c.left
    print("\n|\n".join(res))
    res=[]
    c=root
    while(c):
        p=c
        q=[]
        while(p):
            q.append(p.data)
            p=p.right
        res.append("->".join(q))
        c=c.middle
    print("\n|\n".join(res))
    res=[]
    c=root
    while(c):
        p=c
        q=[]
        while(p):
            q.append(p.data)
            p=p.right
        res.append("->".join(q))
        c=c.right
    print("\n|\n".join(res))

def main():
    root=Node(30)
    root.left=Node(5)
    root.middle=Node(11)
    root.right=Node(63)
    root.left.left=Node(1)
    root.left.middle=Node(4)
    root.left.right=Node(8)
    root.middle.left=Node(6)
    root.middle.middle=Node(7)
    root.middle.right=Node(15)
    root.right.left=Node(31)
    root.right.middle=Node(55)
    root.right.right=Node(65)
    construct(root)
    print_(root)

    
main()