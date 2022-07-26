def getNoSibling(root,res):
    if(root is None):
        return;
    
    if(root.left == None and root.right == None):
        return;
    
    if(root.left):
        getNoSibling(root.left,res)
    else:
        res.append(root.right.data)
    
    if(root.right):
        getNoSibling(root.right,res)
    else:
        res.append(root.left.data)
    

def noSibling(root):
    res = []
    
    getNoSibling(root,res)
    
    res.sort()
    
    return res if len(res) > 0 else [-1]