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

def getGrandChildrenSum(root,mp):
    if(root == None):
        return 0
    sum=0
    if(root.left):
        sum += getMaxSum(root.left.left,mp) + getMaxSum(root.left.right, mp)
    if(root.right):
        sum += getMaxSum(root.right.left, mp) + getMaxSum(root.right.right,mp)

    return sum

def getMaxSum(root, mp):
    if(root == None):
        return 0
    
    if(root in mp):
        return mp[root]
    
    incl = root.data + getGrandChildrenSum(root, mp)

    excl = getMaxSum(root.left, mp) + getMaxSum(root.right, mp)

    mp[root] = max(incl,excl)

    return mp[root]

def main(data):
    data=data.split()
    while('N' in data):
        data[data.index('N')] = '-1'
    data=[int(x) for x in data]
    root=construct(data)
    inorder(root)   
    print()
    print(getMaxSum(root,{}))

main("1 2 3 4 5 6 7")
    

