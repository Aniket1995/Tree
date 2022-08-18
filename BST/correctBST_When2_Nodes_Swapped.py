# just take nodes in inorder list, check the swaped elements in frist go. correct the array and restore the tree
# swap the data of the nodes that it.
# space O(n) time o(n). This solution goes over the array twise in worst case and travrse tree twise. 

def inorder(root, in_, set_):
    if(root == None):
        return 
    inorder(root.left, in_, set_)
    if(set_):
        root.data = in_.pop(0)
    else:
        in_.append(root.data)
    inorder(root.right, in_, set_)
    
    
#Function to fix a given BST where two nodes are swapped.  
class Solution:
    def correctBST(self, root):
        in_=[]
        inorder(root,in_,False)
        len_=len(in_)
        i=0
        j=len_-1
        
        while(i<len_-1 and in_[i] < in_[i+1]):
            i+=1
        
        if(i == len_-1):
            return
        
        while(j>0 and in_[j-1] < in_[j]):
            j-=1
        
        if(j == 0):
            return
        
        in_[i],in_[j] = in_[j],in_[i]
        
        inorder(root,in_,True)

#2 solution
# just take nodes in inorder list, check the elems in one go using (f)irst, (m)id, (l)ast
# in case ajacent vals f and m will be present else f and l
# swap the data of the nodes that it.
# space O(n) time o(n)

def inorder(root, in_):
    if(root == None):
        return 
    inorder(root.left, in_)
    in_.append(root)
    inorder(root.right, in_)
    
#Function to fix a given BST where two nodes are swapped.  
class Solution:
    def correctBST(self, root):
        in_=[]
        inorder(root,in_)
        len_=len(in_)
        f=None
        m=None
        l=None
        
        for i in range(len_-1):
            if(in_[i].data > in_[i+1].data):
                if(not f):
                    f=in_[i]
                    m=in_[i+1]
                else:
                    l=in_[i+1]
        
        if(f and l):
            f.data,l.data = l.data,f.data
        elif(f and m):
            f.data,m.data = m.data,f.data