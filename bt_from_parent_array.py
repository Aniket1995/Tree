'''
Given an array that represents a tree in such a way that array indexes are values in 
tree nodes and array values give the parent node of that particular index (or node).
The value of the root node index would always be -1 as there is no parent for root.
Construct the standard linked representation of given Binary Tree from this given 
representation.
'''


from turtle import left


class Node:
    def __init__(self, data):
        self.key=data
        self.left=None
        self.right=None

# TLE T: o()
# def construct(data):
#     if(len(data) == 0):
#         return None

#     root_data=data.index(-1)
#     root=Node(root_data)
#     q=[root]
#     m={}
#     for i in data:
#         index=data.index(i)   
#         if(i not in m):
#             m[i] = [index]
#         else:
#             m[i].append(index)
#         data[index]='N'
#     # print(m)
#     while(len(q) > 0):
#         n=q.pop(0)
#         if(n.key in m):
#             if(len(m[n.key]) == 2):
#                 n.left=Node(m[n.key][0])
#                 q.append(n.left)
#                 n.right=Node(m[n.key][1])
#                 q.append(n.right)
#             if(len(m[n.key]) == 1):
#                 n.left=Node(m[n.key][0])
#                 q.append(n.left)
#     return root

# # TLE 
# def construct(data):
#     if(len(data) == 0):
#         return None
#     m={}
#     root=None
#     for i in data:
#         index=data.index(i)   
#         if(i not in m):
#             m[i] = [index]
#         else:
#             m[i].append(index)
#         data[index]='N'
#     print(m)
#     root=Node(m[-1][0])
#     m.pop(-1)
#     print(m)
#     construct_bt(root,m)
#     return root

# def construct_bt(root,m):
#     if(root == None):
#         return None
#     if(root.key not in m):
#         return 
#     if(len(m[root.key]) == 2):
#         root.left=Node(m[root.key][0])
#         root.right=Node(m[root.key][1])
#     elif(len(m[root.key]) == 1):
#         root.left=Node(m[root.key][0])
#      construct_bt(root.left, m)
#      construct_bt(root.right, m)




def construct(data):
    l=len(data)
    if(l == 0):
        return None
    m={}
    for i in range(0,l):
        m[i] = Node(i)
    root=None
    for i in range(0,l):
        if(data[i] == -1):
            root=m[i]
        else:
            if(m[data[i]].left == None):
                m[data[i]].left=m[i]
            elif(m[data[i]].right == None):
                m[data[i]].right=m[i]
    return root

def inorder(root):
    if(root == None):
        return 
    inorder(root.left)
    print(root.key,end=" ")
    inorder(root.right)

def preorder(root):
    if(root == None):
        return 
    print(root.key,end=" ")
    preorder(root.left)
    preorder(root.right)

def main(data):
    root=construct(data)
    inorder(root)
    print()
    preorder(root)

main([-1,0,0,1,1,3,5])
