class Node:
    def __init__(self,data):
        self.data=str(data)
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

def getNodeLevel(root, key, lvl):
    if(root == None):
        return -1
    if(root.data == key):
        return lvl
    left = getNodeLevel(root.left,key,lvl+1)
    if(left == -1):
        right = getNodeLevel(root.right,key,lvl+1)
        if(right == -1):
            return -1
        return right
    return left
        

def print_root_leaf_paths(root,s):
    if(root == None):
        return 
    s += root.data + " "
    if(root.left == None and root.right == None):
        print(s)
    print_root_leaf_paths(root.left,s)
    print_root_leaf_paths(root.right,s)

def print_root_leaf_paths_itr(root):
    if(root == None):
        return
    s=[root]

    while(len(s) > 0):
        if(s[-1].left == None and s[-1].right == None):
            print(" ".join(s))
            s.pop()
        if(s[-1] != None):
            if(s[-1].right and s[-1].right not in s):
                s.append(s[-1].right)
            if(s[-1].left and s[-1].left not in s):
                s.append(s[-1].left)
            

    


def print_root_leaf_path_for_key(root,s,key):
    if(root == None):
        return 
    s += root.data + " "
    if(root.data == key):
        print(s)
        return 
    print_root_leaf_path_for_key(root.left,s,key)
    print_root_leaf_path_for_key(root.right,s,key)

def main(data,key):
    data=data.split()
    while('N' in data):
        data[data.index('N')] = '-1'
    data=[int(x) for x in data]
    root=construct(data)
    print()
    inorder(root)
    print()
    print_root_leaf_paths_itr(root)

main("1 2 3 4 5 6 7","4")
main("1 2 3 4 5 6 7","8")
main("1 2 3 4 5 -1 -1 -1 8 6 7 9","8")

main("1 2 3 4 5 -1 -1 -1 8 6 7 9","9")