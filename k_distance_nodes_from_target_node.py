import pathlib
from tkinter.messagebox import NO
from turtle import right


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


def findPath(root,key,path):
    if(root == None):
        return False
    if(root.data == key or findPath(root.left,key,path) or findPath(root.right,key,path)):
        path.append(root)
        return True
    return False

def findKDistNodes(root,k,blocker,res):
    if(root == None or k < 0 or (blocker != None and root == blocker)):
        return
    if( k == 0):
        res.append(root.data)
    findKDistNodes(root.left,k-1,blocker,res)
    findKDistNodes(root.right,k-1,blocker,res)

def main(data,t,k):
    data=data.split()
    while('N' in data):
        data[data.index('N')] = '-1'
    data=[int(x) for x in data]
    root=construct(data)
    print()
    inorder(root)
    print()
    path=[]
    found=findPath(root,t,path)
    for i in path:
        print(i.data, end=" ")
    print()
    res=[]
    if(found):
        for i in range(0,len(path)):
            findKDistNodes(path[i],k-i,path[i-1] if i > 0 else None,res)
    print(res)

    
    



main("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15", "1", 2)


main("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15", "2", 2)


main("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15", "3", 2)


main("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15", "4", 2)

main("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15", "5", 3)
