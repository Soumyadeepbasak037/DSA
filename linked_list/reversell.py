class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class linkedlist:
    def __init__(self) -> None:
        self.head = None

    def print_ll(root):
        while root:
            print(root.data, end="->")
            root = root.next

    def append_ll(root, data):
        while root.next is not None:
            root = root.next
        root.next = Node(data)

    def ll_to_l(root, stack):
        while root:
            stack.append(root.data)
            root = root.next
        print("-------------------")
        print(stack)
