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

def is_leaf(root):
    return root != None and root.left == None and root.right == None

def getNodeLevel(root, key, lvl):
    if(root == None):
        return -1
    if(root.data == key):
        return lvl
    left = getNodeLevel(root.left,key,lvl+1)
    if(left == -1):
        right = getNodeLevel(root.right,key,lvl+1)
        if(right == -1):
            return -1
        return right
    return left
        

def print_cousins(root,key,lvl):
    if(root == None or lvl == -1):
        return
    if(lvl > 1):
        print_cousins(root.left,key,lvl-1)
        print_cousins(root.right,key,lvl-1)
    elif(lvl == 1):
        if((root.left and root.left.data == key) or (root.right and root.right.data == key)):
                return
        if(root.left):
            print(root.left.data,end=" ")
        if(root.right):
            print(root.right.data,end=" ")


def main(data,key):
    data=data.split()
    while('N' in data):
        data[data.index('N')] = '-1'
    data=[int(x) for x in data]
    root=construct(data)
    print()
    inorder(root)
    print('key:{0}'.format(key))
    key_lvl = getNodeLevel(root,key,0)
    print("key lvl:{0}".format(key_lvl))
    print()
    if(key_lvl != -1):
        if(key_lvl == 0):
            print('key is root so no cousins can be printed')
        else:
            print_cousins(root,key,key_lvl)
    else:
        print('key {0} not found'.format(key))
    print()

main("1 2 3 4 5 6 7",'4')
main("1 2 3 4 5 6 7",'1')
main("1 2 3 4 5 6 7",'2')
main("1 2 3 4 5 6 7",'3')
main("1 2 3 4 5 6 7",'5')
main("1 2 3 4 5 6 7",'6')
main("1 2 3 4 5 6 7",'7')
main("1 2 3 4 5 6 7",'70')