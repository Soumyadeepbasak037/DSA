class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


def in_order_traversal(root):
    if root is None:
        return

    in_order_traversal(root.left)
    print(root.data, end=" ")
    in_order_traversal(root.right)


# in_order_traversal(root)


def level_order(root):
    queue = []
    queue.append(root)

    if root is None:
        return

    while (len(queue) > 0):
        print(queue[0].data)
        node = queue.pop(0)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)


level_order(root)
