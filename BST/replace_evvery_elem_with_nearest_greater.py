class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

def insert(root, data):
    global succ
    if(root == None):
        return Node(data)
    if(data < root.data):
        succ=root
        root.left=insert(root.left, data)
    elif(data >= root.data):
        root.right=insert(root.right, data)
    return root

succ=None

class Solution:
    def findLeastGreater(self, n : int, arr : List[int]) -> List[int]:
        global succ
        root=None
        # succ=None
        res=[]
        for i in range(n-1,-1,-1):   
            succ=None
            root=insert(root, arr[i])
            if(succ):
                res.append(succ.data)
            else:
                res.append(-1)
        return reversed(res)