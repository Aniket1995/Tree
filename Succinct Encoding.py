import struct


class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def inorder(root,res):
    if(root == None):
        return
    inorder(root.left,res)
    res.append(root.data)
    inorder(root.right,res)

def construct(data):
    if(len(data) == 0):
        return None
    
    root=Node(data.pop(0))
    q=[root]

    while(len(q) > 0):
        n=q.pop(0)
        if(n.left == None and len(data) > 0):
            if(data[0] != 'N'):
                n.left=Node(data.pop(0))
                q.append(n.left)
            else:
                data.pop(0)
        if(n.right == None and len(data) > 0):
            if(data[0] != 'N'):
                n.right=Node(data.pop(0))
                q.append(n.right)
            else:
                data.pop(0)

    return root

def encode(root, data, struct):
    if(root == None):
        struct.append(0)
    else:
        data.append(root.data)
        struct.append(1)
        encode(root.left, data, struct)
        encode(root.right, data, struct)

def main(data):
    data=data.split()
    root=construct(data)
    res=[]
    inorder(root,res)
    data=[]
    struct=[]
    encode(root,data,struct)
    print(" ".join(res))
    
    print(" ".join(data))
    
    print(" ".join([str(i) for i in struct]))
    

main("1 2 3 4 5 N 6")
# main("7 5 8 2 6 N 56 1 3 N N 10 57 N N N 4 9 51 N N N N N N 13 52 12 45 N 55 11 N 20 49 54 N N N 15 44 48 50 53 N 14 18 23 N 46 N N N N N N N 16 19 21 30 N 47 N 17 N N N 22 28 34 N N N N N N 24 29","__")
# main("1 2 3 4 5 -1 -1 -1 8 6 7 9"," ")
# main("1 2 3 -1 -1 4 5 8 -1 6 7 -1 9"," ")
# main("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15"," ")
# main("1 -1 2 -1 3 -1 4 -1"," ")
# main("1 2 -1 3 -1 4 -1"," ")