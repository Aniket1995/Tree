class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def print_(mat):
    if(mat == None):
        return 
    
    for row in mat:
        print(" ".join(map(str,row)))

def populate(root,mat):
    if(mat == None or root == None):
        return 
    ans=-1
    for i in range(0,7):
        if(mat[i][root.data-1] == 1):
            ans=i
    if(root.left):
        mat[root.data-1][root.left.data-1]=1
        if(ans>=0):
            mat[ans][root.left.data-1]=1
    if(root.right):
        mat[root.data-1][root.right.data-1]=1
        if(ans>=0):
            mat[ans][root.right.data-1]=1
        
    populate(root.left,mat)
    populate(root.right,mat)
    


def main():
    root=Node(7)
    root.left=Node(6)
    root.right=Node(5)
    root.left.left=Node(4)
    root.left.right=Node(3)
    root.right.left=Node(2)
    root.right.right=Node(1)
    mat=[ [0 for i in range(0,7)] for i in range(0,7)]

    print_(mat)
    print("\n")
    populate(root,mat)

    print_(mat)

main()