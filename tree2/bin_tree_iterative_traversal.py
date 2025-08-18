class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


def inorder_iterative(root):
    """Iterative Inorder Traversal: Left, Node, Right"""
    stack = []
    current = root
    result = []  # To store the traversal order
    while current or stack:
        # Reach the leftmost node of the current node
        while current:
            stack.append(current)
            current = current.left
        # Current is None at this point, pop the last node from the stack
        current = stack.pop()
        result.append(current.val)
        # Now, visit the right subtree
        current = current.right
    return result


def preorder_iterative(root):
    """Iterative Preorder Traversal: Node, Left, Right"""
    if not root:
        return []
    stack = [root]
    result = []  # To store the traversal order
    while stack:
        current = stack.pop()
        result.append(current.val)
        # Push right child first so that left is processed first (LIFO)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return result


def postorder_iterative(root):
    """Iterative Postorder Traversal: Left, Right, Node using two stacks"""
    if not root:
        return []
    stack1 = [root]
    stack2 = []
    result = []  # To store the traversal order

    # Process nodes in a modified preorder (Node, Right, Left) and push them into stack2
    while stack1:
        current = stack1.pop()
        stack2.append(current)
        if current.left:
            stack1.append(current.left)
        if current.right:
            stack1.append(current.right)
    # Pop all nodes from stack2 to get the correct postorder sequence
    while stack2:
        result.append(stack2.pop().val)
    return result


if __name__ == "__main__":
    # Build the sample tree:
    #         1
    #        / \
    #       2   3
    #      / \
    #     4   5
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Iterative Inorder Traversal:")
    print(inorder_iterative(root))    # Expected Output: [4, 2, 5, 1, 3]

    print("Iterative Preorder Traversal:")
    print(preorder_iterative(root))   # Expected Output: [1, 2, 4, 5, 3]

    print("Iterative Postorder Traversal:")
    print(postorder_iterative(root))  # Expected Output: [4, 5, 2, 3, 1]
