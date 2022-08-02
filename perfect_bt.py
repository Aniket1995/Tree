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

def node_has_2_children(root):
    if(root == None):
        return True
    if(root.left == None and root.right == None):
        return True
    if(root.left == None or root.right == None):
        return False
    return node_has_2_children(root.left) and node_has_2_children(root.right)

def main(data):
    root=construct(data)
    inorder(root)   
    print()
    print(leaves_at_same_lvl(root,0,[-1]) and node_has_2_children(root))

main([1,2,3])
main([1,2,3,4,5,6,7])
main([5,2,7,1,3,6,10])
main([5,2,7,1,3,6,10,11])