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

def print_level_nodes(root,low,high,lvl):
    if(root == None):
        return 
    q=[root,None]

    while(len(q) > 1):
        node=q.pop(0)
        if(node == None):
            q.append(node)
            print()
            lvl+=1
        else:
            if(node):
                if(lvl >= low and lvl <= high):
                    print(node.data, end=" ")
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)



def main(data,low,high):
    data=data.split()
    while('N' in data):
        data[data.index('N')] = '-1'
    data=[int(x) for x in data]
    root=construct(data)
    print()
    inorder(root)
    print()
    print_level_nodes(root,low,high,1)

main("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15", 1, 1)


main("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15", 2, 3)


main("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15", 3, 4)