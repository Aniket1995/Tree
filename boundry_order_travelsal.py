class Node:
    def __init__(self,data):
        self.data=str(data)
        self.left=None
        self.right=None

def print_left_boundery(root,res):
    if(root == None):
        return 
    if(root.left):
        res.append(root.data)
        print_left_boundery(root.left,res)
    elif(root.right):
        res.append(root.data)
        print_left_boundery(root.right,res)

def print_right_boundry(root,res):
    if(root == None):
        return
    if(root.right):
        print_right_boundry(root.right,res)
        res.append(root.data)
    elif(root.left):    
        print_right_boundry(root.left,res)
        res.append(root.data)

def print_bottom_boundery(root,res):
    if(root == None):
        return
    print_bottom_boundery(root.left,res)
    print_bottom_boundery(root.right,res)
    if(root.left == None and root.right == None):
        res.append(root.data)


def main():
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    root.right.left=Node(6)
    root.right.right=Node(7)
    res=[]
    res.append(root.data)
    print_left_boundery(root.left,res)
    print_bottom_boundery(root.left,res)
    print_bottom_boundery(root.right,res)
    print_right_boundry(root.right,res)
    print(" ".join(res))
main()