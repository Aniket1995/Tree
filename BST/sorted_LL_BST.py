#LinkedList Node
class LNode:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        
#Tree Node        
class TNode:
    def __init__(self, data):
        self.data=data
        self.left = self.right = None
# solution
# tree built from left root right
# time: O(n) space: O(n) (recursion)
def count(head):
    if(head == None):
        return 0
    c=0
    t=head
    while(t):
        c+=1
        t=t.next
    return c

def construct(head_ref, n):
    if(n<=0):
        return None
    left = construct(head_ref, n//2)
    
    root = TNode(head_ref[0].data)
    root.left = left
    head_ref[0] = head_ref[0].next
    
    root.right = construct(head_ref, n-n//2-1)
    
    return root

class Solution:
    def sortedListToBST(self, head):
        head_ref=[head]
        return construct(head_ref, count(head))


#using mid 
# building tree top down
def get_mid(node):
    if(node == None):
        return None, None
    mp=None
    p1=node
    p2=node
    
    while(p2 and p2.next):
        mp=p1
        p1=p1.next
        p2=p2.next
        if(p2):
            p2=p2.next
    return mp,p1

class Solution:
    def sortedListToBST(self, head):
        if(head == None):
            return None
        mp,mid=get_mid(head)
        if(mp == None):
            return TNode(mid.data)
        if(mp and mid):
            root = TNode(mid.data)
            mp.next=None
            root.left=self.sortedListToBST(head)
            root.right=self.sortedListToBST(mid.next)
            return root

