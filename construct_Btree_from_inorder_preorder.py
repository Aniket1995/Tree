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

def constructIt(in_order,pre_order):
    if(len(in_order) == 0 or len(pre_order) == 0):
        return None
    in_=[in_order]
    res=Node(pre_order.pop(0))
    q=[res]
    while(len(q) > 0):
        root=q.pop(0)
        in_order=in_.pop(0)
        if(len(in_order) > 0):
            in_index=in_order.index(root.data)
            left_subtree_in_order=in_order[:in_index]
            right_subtree_in_order=in_order[in_index+1:]
            if(len(left_subtree_in_order) > 0):
                root.left=Node(pre_order.pop(0))
                q.append(root.left)
                in_.append(left_subtree_in_order)
            if(len(right_subtree_in_order) > 0):
                root.right=Node(pre_order.pop(0))
                q.append(root.right)
                in_.append(right_subtree_in_order)
    
    return res


def construct(in_order,pre_order):
    if(len(in_order) == 0 or len(pre_order) == 0):
        return None,pre_order
    root=Node(pre_order.pop(0)) 
    if(root.data in in_order):
        in_index=in_order.index(root.data)
        left_subtree_in_order=in_order[:in_index]
        right_subtree_in_order=in_order[in_index+1:]
        root.left,pre_order=construct(left_subtree_in_order,pre_order)
        root.right,pre_order=construct(right_subtree_in_order,pre_order)
    return root,pre_order

def main(in_order,pre_order):
    root=constructIt(in_order,pre_order)
    inorder(root)
    print()
    preorder(root)

main(["B","A","C"],["A","B","C"])