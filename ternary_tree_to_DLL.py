from re import L


class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.middle=None
        self.right=None

#construct dll accesible only with right pointer
def construct_dll(root):
    if(root == None):
        return None
    left=construct_dll(root.left)
    mid=construct_dll(root.middle)
    right=construct_dll(root.right)
    if(left and mid and right):
        c=left
        while(c.right):
            c=c.right
        c.right=root.middle
        c=mid
        while(c.right):
            c=c.right
        c.right=root.right
        root.right=left
    return root
    
def print_left_and_right(root):
    if(root == None):
        return 
    c=root
    print("right")
    res=[]
    tail=None
    while(c):
        res.append(c.data)
        if(c.right == None):
            tail=c
        c=c.right
    print("->".join(map(str,res)))
    res=[]
    print("left")
    while(tail):
        res.append(tail.data)
        tail=tail.left
    res.reverse()
    print("<-".join(map(str,res)))
    
    

def main():
    root=Node(30)
    root.left=Node(5)
    root.middle=Node(11)
    root.right=Node(63)
    root.left.left=Node(1)
    root.left.middle=Node(4)
    root.left.right=Node(8)
    root.middle.left=Node(6)
    root.middle.middle=Node(7)
    root.middle.right=Node(15)
    root.right.left=Node(31)
    root.right.middle=Node(55)
    root.right.right=Node(65)
    construct_dll(root)
    root.left=None
    c=root
    while(c and c.right):
        c.right.left=c
        c=c.right
    print_left_and_right(root)

    
main()

'''
D:\learning\GFG\Tree>python3 ternary_tree_to_DLL.py
right
30->5->1->4->8->11->6->7->15->63->31->55->65
left
30<-5<-1<-4<-8<-11<-6<-7<-15<-63<-31<-55<-65
'''
