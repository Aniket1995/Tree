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

def postorder(root):
    if(root == None):
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=" ")

def height(root):
    if(root == None):
        return 0
    lh=height(root.left)
    rh=height(root.right)
    if(lh > rh):
        return lh+1
    else:
        return rh+1

def print_level(root,lvl):
    if(root == None):
        return 
    if(lvl < 0):
        return 
    if(lvl == 0):
        print("{0}".format(root.data))
    print_level(root.left,lvl-1)
    print_level(root.right,lvl-1)

def alternate_level_order(root,alt,lvl):
    if(root == None):
        return 
    if(lvl == 0):
        print(root.data,end=" ")
    if(lvl < 0):
        return 
    if(alt):
        alternate_level_order(root.left,alt,lvl-1)
        alternate_level_order(root.right,alt,lvl-1)
    else:
        alternate_level_order(root.right,alt,lvl-1)
        alternate_level_order(root.left,alt,lvl-1)

def build_bst(root,key):
    if(root == None):
        return Node(key)
    if(root.data >= key):
        root.left=build_bst(root.left,key)
    elif(root.data < key):
        root.right=build_bst(root.right,key)
    return root

def build_bt(data):
    root=Node(data.pop(0))
    q=[root]
    i=0
    l=len(data)
    while(len(data) > 0):
        n=q.pop(0)
        if(len(data) > 0 and n.left == None):
            n.left=Node(data.pop(0))
            q.append(n.left)
        if(len(data) > 0 and n.right == None):
            n.right=Node(data.pop(0))
            q.append(n.right)
    
    return root

#The task is to print nodes in level order but nodes should be from left and right side alternatively and from bottom – up manner 
def reverse_lvl_order_with_alt_left_right(root):
    
    if(root == None):
        return []
    
    res=[root.data]
    
    q=[]

    q.append(root.right)
    q.append(root.left)

    alt=True
    while(len(q) >= 2):
        n1=q.pop(0)
        n2=q.pop(0)
        if(n1 and n2):
            res.append(n1.data)
            res.append(n2.data)
            
            q.append(n1.left)
            q.append(n2.right)
            q.append(n1.right)
            q.append(n2.left)
            

    res.reverse()
    return res

def main(data):
    root=build_bt(data)
    inorder(root)
    print()
    # postorder(root)
    print()
    # h=height(root)
    # print()
    # print("height: {0}".format(h))
    # print() 
    # for i in range(0,h):
    #     print("lvl:{0}".format(i))
    #     print_level(root, i)
    print(" ".join(map(str,reverse_lvl_order_with_alt_left_right(root))))
    # alt=True
    # for i in range(0,h):
    #     alt=not alt
    #     alternate_level_order(root,alt,i)
    #     print("lvl: {0}".format(i))



    

# main([1])
# main([2,1,3])
# main([1,2,3])
main([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31])