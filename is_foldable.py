def isFoldable_(r1,r2):
    if(r1 == None and r2 == None):
        return True
    elif(r1 == None or r2 == None):
        return False
    return isFoldable_(r1.left,r2.right) and isFoldable_(r1.right,r2.left)

def IsFoldable(root):
    if(root == None):
        return True
    return isFoldable_(root.left,root.right)