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

def preorder(root):
    if(root == None):
        return
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if(root == None):
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=" ")

# this funtion finds the complete expr in breaces
def find(s,e,expr):
    if(s > e):
        return -1
    stk=[]

    for i in range(s,e+1):
        ch=expr[i]
        if(ch == '('):
            stk.append(ch)
        elif(ch == ')'):
            if(stk[-1] == '('):
                stk.pop()
            
            if(len(stk) == 0):
                return i
    return -1


def construct(expr,s,e):
    if(s > e):
        return None

    root=Node(expr[s])
    index=-1

    if(s+1 <= e and expr[s+1] == '('):
        index=find(s+1,e,expr)
    
    if(index != -1):
        root.left = construct(expr,s+2,index-1)
        root.right = construct(expr,index+2,e-1)
    
    return root
    

def main(expr):
    root=construct(expr,0,len(expr)-1)
    inorder(root)

main("4(2(3)(1))(6(5))")
