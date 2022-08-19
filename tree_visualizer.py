class Node:
    def __init__(self,data):
        self.data=int(data)
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
            if(data[0] != '-1'):
                n.left=Node(data.pop(0))
                q.append(n.left)
            else:
                data.pop(0)
        if(n.right == None and len(data) > 0):
            if(data[0] != '-1'):
                n.right=Node(data.pop(0))
                q.append(n.right)
            else:
                data.pop(0)

    return root

def is_leaf(root):
    return root != None and root.left == None and root.right == None

def merge(a,b,ch):
    if(a is None):
        return b
    if(b is None):
        return a
    for i in range(0,len(b)):
        if(str(b[i]) == ch and a[i] != ch):
            b[i] = a[i]

def build_level_map(root,m,in_order,lvl,ch):
    if(root == None):
        return None
    curr=[]
    # if(lvl > 0):
    #     ch = ch*2
    for i in in_order:
        curr.append(str(i) if i == root.data else ch)
    if(lvl not in m):
        m[lvl] = curr
    else:
        merge(curr,m[lvl],ch)
    
    build_level_map(root.left,m,in_order,lvl+1,ch)
    build_level_map(root.right,m,in_order,lvl+1,ch)

def visualize(root, ch):
    in_order=[]
    inorder(root,in_order)
    print()
    m={}
    build_level_map(root,m,in_order,0,ch)
    # print(m)
    for k,v in m.items():
        print("".join(v)) 

def main(data,ch):
    data=data.split()
    while('N' in data):
        data[data.index('N')] = '-1'
    # data=[int(x) for x in data]
    root=construct(data)
    visualize(root, ch)
    

# main("1 2 3 4 5 6 7 8 9 12 N N N N N N N 13 14 N 11 N N 15", "_")
# main("7 5 8 2 6 N 56 1 3 N N 10 57 N N N 4 9 51 N N N N N N 13 52 12 45 N 55 11 N 20 49 54 N N N 15 44 48 50 53 N 14 18 23 N 46 N N N N N N N 16 19 21 30 N 47 N 17 N N N 22 28 34 N N N N N N 24 29","__")
# main("1 2 3 4 5 -1 -1 -1 8 6 7 9"," ")
# main("1 2 3 -1 -1 4 5 8 -1 6 7 -1 9"," ")
# main("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15"," ")
# main("1 -1 2 -1 3 -1 4 -1"," ")
# main("1 2 -1 3 -1 4 -1","_")