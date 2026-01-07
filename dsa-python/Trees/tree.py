'''Note: 
Left < Parent
Right > Parent

'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Node(10)

root.left = Node(5)
root.right = Node(15)

root.left.left = Node(2)
root.left.right = Node(7)

root.right.right = Node(20)


# Binary Search Tree

def binary_search_tree(Node, target):
    if Node is None:
        return False
    
    if Node.value == target:
        return True
    elif target < Node.value:
        return binary_search_tree(Node.left, target)
    else:
        return binary_search_tree(Node.right, target)
    

print(binary_search_tree(root, 7))  # True 
print(binary_search_tree(root, 12))  # False


# In order Traversal
def in_order_traversal(Node):
    if Node is None:
        return
    
    in_order_traversal(Node.left)
    print(Node.value)
    in_order_traversal(Node.right)

in_order_traversal(root)