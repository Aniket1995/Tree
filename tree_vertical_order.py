class Node:
    def __init__(self, data):
        self.data = str(data)
        self.left = None
        self.right = None


def inorder(root):
    if(root == None):
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


def construct(data):
    if(len(data) == 0):
        return None

    root = Node(data.pop(0))
    q = [root]

    while(len(q) > 0):
        n = q.pop(0)
        if(n.left == None and len(data) > 0):
            if(data[0] != -1):
                n.left = Node(data.pop(0))
                q.append(n.left)
            else:
                data.pop(0)
        if(n.right == None and len(data) > 0):
            if(data[0] != -1):
                n.right = Node(data.pop(0))
                q.append(n.right)
            else:
                data.pop(0)

    return root


def get_vertical_order(root, m, v, l):
    if(root == None):
        return
    if(v in m.keys()):
        if(l in m[v].keys()):
            m[v][l].append(root.data)
        else:
            m[v][l] = [root.data]
    else:
        m[v] = {l:[root.data]}
    get_vertical_order(root.left, m, v-1, l+1)
    get_vertical_order(root.right, m, v+1, l+1)


def main(data):
    data = data.split()
    while('N' in data):
        data[data.index('N')] = '-1'
    data = [int(x) for x in data]
    root = construct(data)
    print()
    inorder(root)
    print()
    m = {}
    get_vertical_order(root, m, 0, 1)
    res=[]
    for vertical in sorted(m.keys()):
        for level in sorted(m[vertical].keys()):
            res += m[vertical][level]
    print(" ".join(res))


main("1 2 3 4 5 -1 6")
main("1 2 3 4 5 -1 -1 -1 8 6 7 9")
