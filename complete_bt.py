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

def is_leaf(root):
    return root != None and root.left == None and root.right == None

def complete_bt(root):
    if(root == None):
        return True

    flg=False
    q=[root]
    while(len(q) > 0):
        n=q.pop(0)
        if(n != None):
            if(flg):
                return False
            q.append(n.left)
            q.append(n.right)
        else:
            flg=True
    return True

def main(data):
    root=construct(data)
    inorder(root)   
    print()
    print(complete_bt(root))

main([1,2,3,4,5])
main([1,2,3,4,5,6,7])
main([5,2,7,1,3,6,10])
main([5,2,7,1,3,6,10,11])
main([1,-1,2,3])
main([1,2,3,4,5,6,7,-1,-1,9])
main([5,2,7,1,3,6,10,-1,-1,8])
main([5,2,7,1,3,6,10,-1,11])