def optCost(freq, i, j, costs):
     
    # Base cases
    if j < i:     # no elements in this subarray
        return 0

    if(costs[i][j] > 0):
        return costs[i][j]
    
    if j == i:
        costs[i][j]=freq[i]
        return freq[i]
     
    # Get sum of freq[i], freq[i+1], ... freq[j]
    fsum = Sum(freq, i, j)
     
    # Initialize minimum value
    Min = 999999999999
     
    # One by one consider all elements as
    # root and recursively find cost of
    # the BST, compare the cost with min
    # and update min if needed
    for r in range(i, j + 1):
        cost = (optCost(freq, i, r - 1, costs) +
                optCost(freq, r + 1, j, costs))
        if cost < Min:
            Min = cost
     
    costs[i][j] = Min + fsum
    # Return minimum value
    return costs[i][j]
 
def Sum(freq, i, j):
    s = 0
    for k in range(i, j + 1):
        s += freq[k]
    return s

# The main function that calculates minimum
# cost of a Binary Search Tree. It mainly
# uses optCost() to find the optimal cost.
def optimalSearchTree(keys, freq, n):

    # Here array keys[] is assumed to be
    # sorted in increasing order. If keys[]
    # is not sorted, then add code to sort 
    # keys, and rearrange freq[] accordingly.
    n=len(freq)
    costs = [[-1]*(5) for i in range(n)]
    print(costs)
    return optCost(freq, 0, n - 1, costs)


def main(keys, freq):
    keys=[int(i) for i in keys.split()]
    freq=[int(i) for i in freq.split()]
    
    print(optimalSearchTree(keys, freq, len(freq)))



main("1 4 5 32 34", "39 14 40 14 12")

