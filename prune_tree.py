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

def prune(root,k,pathSum):
    if(root == None):
        return True
    pathSum += root.data
    if(root.left == None and root.right == None):
        if(k > pathSum):
            return True
        return False
    left = prune(root.left,k,pathSum)
    if(left):
        root.left = None
    right = prune(root.right,k,pathSum)
    if(right):
        root.right = None
    if(left and right):
        return True
    return False

# sum longest leaf to root path


def main(data, k):
    data=data.split()
    while('N' in data):
        data[data.index('N')] = '-1'
    data=[int(x) for x in data]
    root=construct(data)
    print()
    inorder(root)
    print()
    prune(root,k,0)
    print()
    inorder(root)
    print()


# main("1 2 3 4 5 6 7", 10)
# main("1 2 3 4 5 6 7 -1 8 -1 -1 -1 -1 -1", 10)

main("1 2 3 4 5 6 7 8 9 12 -1 -1 -1 10 -1 -1 -1 13 14 -1 -1 -1 11 -1 -1 15", 20)

main("1 2 3 4 5 6 7 8 9 12 -1 -1 -1 10 -1 -1 -1 13 14 -1 -1 -1 11 -1 -1 15", 45)