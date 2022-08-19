class Node:
    def __init__(self,data):
        self.data=int(data)
        self.left=None
        self.right=None
        self.height=1

def get_balance(root):
    if(root == None):
        return 0
    return height(root.left) - height(root.right)

def height(root):
    if(root == None):
        return 0
    return root.height

def inorder(root,res):
    if(root == None):
        return
    inorder(root.left,res)
    res.append(root.data)
    inorder(root.right,res)

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
        curr.append(str(i)+"({0})".format(root.height) if i == root.data else ch)
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

def leftRotate(x):
    y=x.right
    T2=y.left

    y.left=x
    x.right=T2

    x.height = max(height(x.left), height(x.right)) + 1
    y.height = max(height(y.left), height(y.right)) + 1

    return y

def rightRotate(y):
    x=y.left
    T2=x.right

    x.right=y
    y.left=T2

    y.height = max(height(y.left), height(y.right)) + 1
    x.height = max(height(x.left), height(x.right)) + 1

    return x    

def insert(root, key):
    if(root == None):
        return Node(key)
    if(root.data < key):
        root.right=insert(root.right, key)
    elif(root.data > key):
        root.left=insert(root.left, key)
    # else:
    #     return root
    root.height = 1 + max(height(root.left), height(root.right))
    balance = get_balance(root)
    if(balance > 1 and key < root.left.data):
        print("\nLL case\n")
        visualize(root, '_'*(3+len(str(root.data))))
        return rightRotate(root)
    if(balance > 1 and key > root.left.data):
        print("\nLR case\n")
        visualize(root, '_'*(3+len(str(root.data))))
        root.left=leftRotate(root.left)
        print("\nLL case\n")
        visualize(root, '_'*(3+len(str(root.data))))
        return rightRotate(root)
    if(balance < -1 and root.right.data < key):
        print("\nRR case\n")
        visualize(root, '_'*(3+len(str(root.data))))
        return leftRotate(root)
    if(balance < -1 and root.right.data > key):
        print("\nRL case\n")
        visualize(root, '_'*(3+len(str(root.data))))
        root.right=rightRotate(root.right)
        print("\nRR case\n")
        visualize(root, '_'*(3+len(str(root.data))))
        return leftRotate(root)
    return root

def main(data):
    root = None
    for i in data.split():
        print("\ninserting {0}".format(i))
        root = insert(root, int(i))
        print("\n final tree structure: \n")
        visualize(root, '_'*(3+len(str(root.data))))
    print()

# main("1 2 3 4 5 6 7 8 9")

# main("366 359 344 496 270 213")

# main("9 8 7 6 5 4 3 2 1")

# main("1 4 2 5 3 6 9 8 7")

main("209 312 799 352 427 607 379 381 332 943 119 220")

'''
inserting 209

 final tree structure: 


209(1)

inserting 312

 final tree structure: 


209(2)______
______312(1)

inserting 799

RR case


209(3)____________
______312(2)______
____________799(1)

 final tree structure: 


______312(2)______
209(1)______799(1)

inserting 352

 final tree structure: 


______312(3)____________
209(1)____________799(2)
____________352(1)______

inserting 427

LR case


____________799(3)
352(2)____________
______427(1)______

LL case


____________799(3)
______427(2)______
352(1)____________

 final tree structure:


______312(3)__________________
209(1)____________427(2)______
____________352(1)______799(1)

inserting 607

RR case


______312(4)________________________
209(1)____________427(3)____________
____________352(1)____________799(2)
________________________607(1)______

 final tree structure:


__________________427(3)____________
______312(2)__________________799(2)
209(1)______352(1)______607(1)______

inserting 379

 final tree structure:


________________________427(4)____________
______312(3)________________________799(2)
209(1)______352(2)____________607(1)______
__________________379(1)__________________

inserting 381

RR case


352(3)____________
______379(2)______
____________381(1)

 final tree structure:


______________________________427(4)____________
______312(3)______________________________799(2)
209(1)____________379(2)____________607(1)______
____________352(1)______381(1)__________________

inserting 332

RL case


______312(4)________________________
209(1)__________________379(3)______
__________________352(2)______381(1)
____________332(1)__________________

RR case


______312(4)________________________
209(1)____________352(3)____________
____________332(1)______379(2)______
______________________________381(1)

 final tree structure:


____________________________________427(4)____________
__________________352(3)________________________799(2)
______312(2)____________379(2)____________607(1)______
209(1)______332(1)____________381(1)__________________

inserting 943

 final tree structure:


____________________________________427(4)__________________
__________________352(3)________________________799(2)______
______312(2)____________379(2)____________607(1)______943(1)
209(1)______332(1)____________381(1)________________________

inserting 119

LL case


__________________________________________427(5)__________________
________________________352(4)________________________799(2)______
____________312(3)____________379(2)____________607(1)______943(1)
______209(2)______332(1)____________381(1)________________________
119(1)____________________________________________________________

 final tree structure:


________________________352(4)____________________________________
____________312(3)________________________427(3)__________________
______209(2)______332(1)______379(2)__________________799(2)______
119(1)______________________________381(1)______607(1)______943(1)

inserting 220

 final tree structure:


______________________________352(4)____________________________________
__________________312(3)________________________427(3)__________________
______209(2)____________332(1)______379(2)__________________799(2)______
119(1)______220(1)________________________381(1)______607(1)______943(1)

'''