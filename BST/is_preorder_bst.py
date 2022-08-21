import math
class Solution:

    def canRepresentBST(self, arr, N):
        # Create an empty stack
        s = []
    
        # Initialize current root as minimum possible value
        root = -2**32-1
    
        # Traverse given array
        for value in arr:
            #NOTE:value is equal to pre[i] according to the
            #given algo  
        
            # If we find a node who is on the right side
            # and smaller than root, return False
            if value < root :
                return 0
        
            # If value(pre[i]) is in right subtree of stack top,
            # Keep removing items smaller than value
            # and make the last removed items as new root
            while(len(s) > 0 and s[-1] < value) :
                root = s.pop()
            
            # At this point either stack is empty or value
            # is smaller than root, push value
            s.append(value)
    
        return 1

def main(data):
    data=list(map(int,data.split()))
    N=len(data)
    print(Solution().canRepresentBST(data, N))

main("2 4 3")

main("2 4 1")

main("3 2 4 6 7 12 14")

main("7 2 4 8")