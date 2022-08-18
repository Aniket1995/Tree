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
        