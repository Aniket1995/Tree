from re import L


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
    

def find_node_with_2_children(root):
    if(root == None):
        return root
    if(root.left != None and root.right != None):
        return root
    left = find_node_with_2_children(root.left)
    if(left == None):
        right = find_node_with_2_children(root.right)
        return right
    return left

def print_longest_path_left_leaf(root,s,flg):
    if(root == None):
        return ""
    if(flg[0] == 0):
        if(root.left):
            s = print_longest_path_left_leaf(root.left,s,flg)
        elif(root.right):
            s = print_longest_path_left_leaf(root.right,s,flg)
        s += root.data + " "
    else:
        s += root.data + " "
        if(root.right):
            s = print_longest_path_left_leaf(root.right,s,flg)
        elif(root.left):
            s = print_longest_path_left_leaf(root.left,s,flg)
    return s
    

def print_longest_leaf_to_leaf_paths(root):
    node_with_2_children=find_node_with_2_children(root)
    print(print_longest_path_left_leaf(node_with_2_children,"",[0]),end="")
    
    print(print_longest_path_left_leaf(node_with_2_children,"",[1])[2:])

    
def main(data):
    data=data.split()
    while('N' in data):
        data[data.index('N')] = '-1'
    data=[int(x) for x in data]
    root=construct(data)
    print()
    inorder(root)
    print()
    print_longest_leaf_to_leaf_paths(root)

main("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20")
main("1 2 3 4 5 -1 -1 -1 8 6 7 9")