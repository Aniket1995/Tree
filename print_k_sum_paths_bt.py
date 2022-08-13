
'''
Input : k = 5  
        Root of below binary tree:
           1
        /     \
      3        -1
    /   \     /   \
   2     1   4     5                        
        /   / \     \                    
       1   1   2     6    
Input : 1 3 -1 2 1 4 5 N N 1 N 1 2 N 6     k=5                  
Output :
3 2 
3 1 1 
1 3 1 
4 1 
1 -1 4 1 
-1 4 2 
5 
1 -1 5 
'''

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

def printKSumPath(root,path,k):
    if(root == None):
        return 
    
    path.append(root.data)

    printKSumPath(root.left, path, k)

    printKSumPath(root.right, path, k)

    sum=0
    for i in range(len(path)-1, -1, -1):
        sum += int(path[i])
        if(sum == k):
            print("\n"+" ".join(path[i:]))
    path.pop()

def main(data,k):
    data=data.split()
    root=construct(data)
    inorder(root)
    path=[]
    printKSumPath(root,path,k)

main("1 2 3 4 5 6 7", 5)
main("1 3 -1 2 1 4 5 N N 1 N 1 2 N 6", 5)
# main("1 2 3 4 5 2 N N N N N 4 5")