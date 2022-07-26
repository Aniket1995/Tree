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


def construct(in_order,lvl_order):
    if(len(in_order) == 0 or len(lvl_order) == 0):
        return None
    res=Node(lvl_order.pop(0))
    q=[res]
    in_=[in_order]
    while(len(q) > 0):
        root=q.pop(0)
        in_order=in_.pop(0)
        if(root.data in in_order):
            root_index=in_order.index(root.data)
            left_tree_in_order=in_order[:root_index]
            right_tree_in_order=in_order[root_index+1:]
            if(len(left_tree_in_order) > 0):
                root.left=Node(lvl_order.pop(0))
                q.append(root.left)
                in_.append(left_tree_in_order)
            if(len(right_tree_in_order) > 0):
                root.right=Node(lvl_order.pop(0))
                q.append(root.right)
                in_.append(right_tree_in_order)
    return res
    

def main(in_order,lvl_order):
    root=construct(in_order,lvl_order)
    inorder(root)
    print()
    preorder(root)

main([4, 8, 10, 12, 14, 20, 22],[20, 8, 22, 4, 12, 10, 14])