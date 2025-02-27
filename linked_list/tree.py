class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder_traversal(root, arr):
    if root:
        arr.append(root)
        preorder_traversal(root.left, arr)
        preorder_traversal(root.right, arr)

def flatten(root):
    if not root:
        return None

    arr = []
    preorder_traversal(root, arr)

    for i in range(len(arr) - 1):
        arr[i].right = arr[i + 1]
        arr[i].left = None
    
    arr[-1].right = None  # Last node's right should be None
    arr[-1].left = None   # Last node's left should also be None

# Helper function to print the linked list
def print_linked_list(root):
    while root:
        print(root.val, end=" -> ")
        root = root.right
    print("None")

# Example usage:
# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)

# Flatten the binary tree to linked list
flatten(root)

# Print the flattened linked list
print_linked_list(root)
