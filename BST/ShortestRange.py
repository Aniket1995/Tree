from collections import defaultdict
import heapq

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def insert(root, key):
    if(root == None):
        return Node(key)
    if(root.data < key):
        root.right = insert(root.right, key)
    if(root.data > key):
        root.left = insert(root.left, key)
    return root

def inorder(root):
    if(root == None):
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)

def populate_inorder(root,res):
    if(root == None):
        return
    populate_inorder(root.left,res)
    res.append(root.data)
    populate_inorder(root.right,res)

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
    for i in in_order:
        curr.append(str(i) if i == root.data else ch)
    if(lvl not in m):
        m[lvl] = curr
    else:
        merge(curr,m[lvl],ch)
    
    build_level_map(root.left,m,in_order,lvl+1,ch)
    build_level_map(root.right,m,in_order,lvl+1,ch)

def visualize(root, ch):
    in_order=[]
    populate_inorder(root,in_order)
    print()
    m={}
    build_level_map(root,m,in_order,0,ch)
    for k,v in m.items():
        print("".join(v))

# def inorder_(root, inArr, lvlSet, lvl):
#     if(root == None):
#         return 
#     inorder_(root.left, inArr, lvlSet, lvl+1)
#     inArr.append([root.data, lvl])
#     lvlSet.add(lvl)
#     inorder_(root.right, inArr, lvlSet, lvl+1)


# def thisIsAns(freq, levels):
#     for i in range(levels):
#         if(freq[i] > 0):
#             continue
#         return False
#     return True

# def findMinRange(root):
#     inArr=[]
#     lvlSet=set()
#     inorder_(root, inArr, lvlSet, 1)
#     n=len(inArr)
#     if(n == 1):
#         return [root.data, root.data]
#     levels=len(lvlSet)
#     i=0
#     j=i
#     ans=None
#     min=0
#     freq=[0]*levels
#     flg=True
#     while(i <= j and j < n):
#         if(flg):
#             freq[inArr[j][1]-1]+=1
#         if(thisIsAns(freq, levels)):
#             p_ans=[inArr[i][0], inArr[j][0]]
#             p_min = p_ans[1] - p_ans[0]
#             if(ans is None):
#                 ans = p_ans
#                 min=p_min
#             elif(p_min < min):
#                 ans = p_ans
#                 min=p_min
#             elif(p_min == min and p_ans[0] < ans[0]):
#                 ans=p_ans
#             freq[inArr[i][1]-1]-=1
#             i+=1
#             flg=False
#             continue
#         flg=True
#         j+=1
#     return ans



def level_order(root,dic,level):
    if root==None:
        return
    dic[level].append(root.data)
    level_order(root.left,dic,level+1)
    level_order(root.right,dic,level+1)
    
def shortestRange( root):
    # Return pair/tuple of range
    # Your code goes here
    dic=defaultdict(list)
    level_order(root,dic,0)
    heap=[]
    mn,mx=float('inf'),0
    for i in range(len(dic)):
        heapq.heappush(heap,[dic[i][0],i,1])
        mn=min(mn,dic[i][0])
        mx=max(mx,dic[i][0])
        dic[i].append(float('inf'))
    ans=[mn,mx]
    while heap:
        h=heapq.heappop(heap)
        heapq.heappush(heap,[dic[h[1]][h[2]],h[1],h[2]+1])
        mx=max(mx,dic[h[1]][h[2]])
        if (ans[1]-ans[0])>(mx-heap[0][0] ):
            ans=[heap[0][0],mx]
            if (ans[1]-ans[0])==0:
                return ans
        if mx==float('inf'):
            return ans
    return ans
    
def main(data):
    root = None
    for i in data.split():
        root = insert(root, int(i))
    inorder(root)
    visualize(root, '_')
    print(shortestRange(root))
    print()

# main("35")

main("8 3 10 2 6 14 4 7 12 11 13") # [6, 11]

# main("11 12 13 14 15 16") # [11, 16]

# main("15 10 20 5 13 18 25 2 6 16 19 30") # 15 20

# main("63 32 4 33 1") # 1 63

# main("40 1 54 22 52 60 21 32 45 53") # 40 54

# main("35 2 76 1 29 50 79 9 32") # 2 35
        


