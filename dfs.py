import random

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


nodes = [Node(i) for i in range(10)]

nodes[0].left = nodes[1]
nodes[0].right = nodes[2]
nodes[1].left = nodes[3]
nodes[1].right = nodes[4]
nodes[3].left = nodes[7]
nodes[2].left = nodes[5]
nodes[2].right = nodes[6]
nodes[6].right = nodes[8]

def show_nodes(root, d):
    if root is None:
        return 
    
    print(d, root)
    show_nodes(root.left, 'left')
    show_nodes(root.right, 'right')

def dfs(root, goal, path=[], popped=[], sender_node_val=0):
    print(root, path)
    if goal.value in path:
        return path
    if not root:
        if sender_node_val not in popped:
            popped.append(sender_node_val)
            path.pop()
        return []
    
    path.append(root.value)

    l = dfs(root.left, goal, path, popped, root.value) 
    r = dfs(root.right, goal, path, popped, root.value)
    
    if goal.value in l:
        return l
    elif goal.value in r:
        return r
    return []
    



# show_nodes(nodes[0], 'root')

print(dfs(nodes[0], nodes[int(input('Node: '))]))