import random


class Node:
    def __init__(self, value, left=None, right=None, has_conn=False):
        self.value = value
        self.left = left
        self.right = right
        self.has_conn = has_conn

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

def show_nodes(root):
    if root is None:
        return 
    
    print(root)
    show_nodes(root.left)
    show_nodes(root.right)

def dfs(root, goal, path=[]):
    if root == goal:
        return path
    if root == None:
        return []
    
    path.append(root.value)
    dfs(root.left, goal, path)
    dfs(root.right, goal, path)

print(dfs(nodes[0], nodes[4]))