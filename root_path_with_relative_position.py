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

def get_min_max_vertical_order(root,v,maxV,minV):
    if(root == None):
        return 
    minV[0] = v if v < minV[0] else minV[0]
    maxV[0] = v if v > maxV[0] else maxV[0]
    get_min_max_vertical_order(root.left,v-1,maxV,minV)
    get_min_max_vertical_order(root.right,v+1,maxV,minV)

def is_leaf(root):
    return root != None and root.left == None and root.right == None

def print_relative_order(root,m,v):
    if(root == None):
        return
    m[root.data] = v
    if(is_leaf(root)):
        minV = min(m.values())
        maxV = max(m.values())
        for k,v in m.items():
            if(v <= 0):
                print("_"*(abs(minV)-abs(v))+k)
            else:
                if(minV >= 0):
                    print("_"*(v)+k)
                else:
                    print("_"*(v+maxV)+k)
        print()
    print_relative_order(root.left,m,v-1)
    print_relative_order(root.right,m,v+1)
    m.pop(root.data)
            

def main(data):
    data=data.split()
    while('N' in data):
        data[data.index('N')] = '-1'
    data=[int(x) for x in data]
    root=construct(data)
    print()
    inorder(root)
    print()
    m={}
    print_relative_order(root,m,0)
    

main("1 2 3 4 5 6 7")
main("1 2 3 4 5 -1 -1 -1 8 6 7 9")
main("1 2 3 -1 -1 4 5 8 -1 6 7 -1 9")