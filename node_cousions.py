class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def getLevelAndParent(root,key):
    if(root == None):
        return 0,None
    if(root.left != None and root.left.data == key):
        return 1,root
    if(root.right != None and root.right.data == key):
        return 1,root
    llvl,p=getLevelAndParent(root.left,key)
    if(p == None):
        rlvl,p=getLevelAndParent(root.right,key)
        if(p == None):
            return 0,None
        return (rlvl+1),p
    return (llvl+1),p

def inorder(root):
    if(root == None):
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)

def isCousin(root, a, b):
    # inorder(root)
    # print()
    alvl,ap=getLevelAndParent(root,a)
    # print("alvl:{0}, ap:{1}".format(alvl,ap.data))
    blvl,bp=getLevelAndParent(root,b)
    # print("blvl:{0}, bp:{1}".format(blvl,bp.data))
    
    if(ap != bp and alvl == blvl):
        return 1
    else:
        return 0

def construct(data):
    if(len(data) == 0):
        return None
    
    root=Node(data.pop(0))
    q=[root]

    while(len(q) > 0):
        n=q.pop(0)
        if(n.left == None and len(data) > 0):
            n.left=Node(data.pop(0))
            q.append(n.left)
        if(n.right == None and len(data) > 0):
            n.right=Node(data.pop(0))
            q.append(n.right)

    return root

def inorder(root):
    if(root == None):
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)

def main(data,a,b):
    root=construct(data)
    inorder(root)   
    print()
    print(isCousin(root,a,b))

main([1,2,3,4,5,6,7],4,6)