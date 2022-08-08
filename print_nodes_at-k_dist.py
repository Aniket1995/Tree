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

def print_nodes(root,k,visited,path,pathLen,cnt):
    if(root == None):
        return 
    path[pathLen] = root.data
    visited[pathLen] = False
    pathLen += 1
    kth_node = pathLen - k - 1
    if(root.left == None and root.right == None and (kth_node) >= 0 and visited[kth_node] == False):
        cnt[0] +=1
        visited[kth_node] = True
        return
    print_nodes(root.left,k,visited,path,pathLen,cnt)
    print_nodes(root.right,k,visited,path,pathLen,cnt)
    

    
def main(data,k):
    data=data.split()
    while('N' in data):
        data[data.index('N')] = '-1'
    data=[int(x) for x in data]
    root=construct(data)
    print()
    inorder(root)
    print()
    cnt=[0]
    visited = [None] * 1000
    path = [None] * 1000
    print_nodes(root,k,visited,path,0,cnt)
    print(cnt[0])

    
    
main("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15", 1)

