class Node():
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None

import math

def findmax(root):
    if root == None:
        return -math.inf
    else:
        return max(root.key, findmax(root.left), findmax(root.right))



root = Node(10)
root.left = Node(80)
root.right = Node(15)
root.right.left = Node(40)
print(findmax(root))