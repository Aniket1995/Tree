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

def print_nodex_at_k_dist_from_root(root,k):
    if(root == None):
        return 
    q=[root,None]
    lvl=0
    while(len(q) > 1 and lvl <= k):
        n=q.pop(0)
        if(n == None):
            q.append(n)
            lvl+=1
        else:
            if(k == lvl):
                print(n.data,end=" ")
            if(n.left):
                q.append(n.left)
            if(n.right):
                q.append(n.right)



def main(data,k):
    data=data.split()
    while('N' in data):
        data[data.index('N')] = '-1'
    data=[int(x) for x in data]
    root=construct(data)
    print()
    inorder(root)
    print()
    print_nodex_at_k_dist_from_root(root,k)

main("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15", 1)


main("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15", 2)


main("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15", 3)


main("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15", 4)


main("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15", 0)