class Node():
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next


root = Node(1)
root.next = Node(2)
root.next.next = Node(4)

root2 = Node(1)
root2.next = Node(3)
root2.next.next = Node(4)


def print_list(root: Node):
    while (root != None):
        print(root.data, end="->")
        root = root.next
    print("\n")


# def append(root: Node, val):
#     new_node = Node(val)
#     if root is None:
#         # root = new_node
#         return new_node
#     else:
#         while (root.next != None):
#             root = root.next
#         root.next = new_node
#         return

# req_root = Node()
# append(root, 55)

# def append(root: Node, data):
    new_node = Node(data)

    if root is None:
        return new_node

    current = root
    while current.next is not None:
        current = current.next

    current.next = new_node

    return root


def ll_l(root, arr):
    while root is not None:
        arr.append(root.data)
        # print(root.data, end="->")
        root = root.next


# print_list(root)
# print_list(root2)
arr1 = []
arr2 = []
# ll_l(root, arr1)
# ll_l(root2, arr2)

req_node = None
# append(req_node, 5)7
print_list(req_node)
# for i in range(min(len(arr1), len(arr2))):
#     if (arr1[i] > arr2[i]):
