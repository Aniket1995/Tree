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

def leaves_at_same_lvl(root,lvl,fll):
    if(root == None):
        return True
    if(root.left == None and root.right == None):
        if(fll[0] == -1):
            fll[0] = lvl
            return True
        elif(fll[0] != lvl):
            return False
        return True
    return leaves_at_same_lvl(root.left,lvl+1,fll) and leaves_at_same_lvl(root.right,lvl+1,fll)

def main(data):
    root=construct(data)
    inorder(root)   
    print()
    print(leaves_at_same_lvl(root,0,[-1]))

main([1, 2, -1, 3, 4, -1, 5, 6, -1, 7, 8, -1, 9, 10, -1, 11, 12, -1, 13, 14, -1, 15, 16, -1, 17, 18])