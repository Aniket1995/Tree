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

def duplicate_subtree(root,marker,subtrees):
    print(subtrees)
    if(root == None):
        return marker,False

    lstr,found = duplicate_subtree(root.left,marker,subtrees)

    if(found):
        return lstr,found

    rstr,found = duplicate_subtree(root.right,marker,subtrees)

    if(found):
        return rstr,found

    s = root.data + marker + lstr + rstr

    print(s)

    if(len(s.split()) >= 2  and s in subtrees):
        return s,True

    subtrees[s] = 1

    return s,False
    

def main(data):
    data=data.split()
    while('N' in data):
        data[data.index('N')] = '-1'
    data=[int(x) for x in data]
    root=construct(data)
    inorder(root)   
    print()
    print(duplicate_subtree(root,' ',{}))

# main("1 2 3 4 5 2 N N N N N 4 5")
# main("1 2 3 4 N 2 N N N 4 N")
# main("27 41 11 5 26 45 46 16 10 12 7 15 30 11 28 48 32 28 18 32 3 N 7 36 5 39 12 47 32 30 23 17 45 13 22 20 45 36 23")
main("81 88 79 84 64 85 54 48 33 74 6 18 21 65 93 40 63 82 55 16 26 76 1 6 46 24 57 62 76 71 69 47 41 N 61 80 79 20 62 40 29 3 52 70 99 73 69 100 7 46 87 45 100 7 97 70 28 45 83")