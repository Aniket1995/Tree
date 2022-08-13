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

def getPath(root, res, s):
    if(root == None):
        return
    s += str(root.data) + " "
    if(root.left == None and root.right == None):
        res.append(s.split())
    getPath(root.left,res,s)
    getPath(root.right,res,s)

def sum(root,pathSum,maxLvl,lvl,res):
    if(root == None):
        return
    currSum = pathSum + root.data
    if(root.left == None and root.right == None):
        if(maxLvl[0] < lvl):
            res[0] = currSum
            maxLvl[0] = lvl
    sum(root.left,currSum,maxLvl,lvl+1,res)
    sum(root.right,currSum,maxLvl,lvl+1,res)

# sum longest leaf to root path

def main(data):
    data=data.split()
    while('N' in data):
        data[data.index('N')] = '-1'
    data=[int(x) for x in data]
    root=construct(data)
    print()
    inorder(root)
    print()
    # 1.Solution - all paths and max from the path lens
    # allPaths = []
    # getPath(root,allPaths, "")
    # print(allPaths)
    # res = None
    # max = 0
    # for path in allPaths:
    #     l = len(path)
    #     if(l > max):
    #         res = path
    #         max = l
    # print(sum([int(i) for i in res]))

    res=[0]
    sum(root,0,[0],0,res)
    print(res[0])


main("1 2 3 4 5 6 7")
main("1 2 3 4 5 6 7 -1 8 -1 -1 -1 -1 -1")