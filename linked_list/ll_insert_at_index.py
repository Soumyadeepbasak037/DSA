class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_index(self, index, data):
        new_node = Node(data)
        # Inserting at the head (index 0)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        # Move to the node just before the target index
        for i in range(index - 1):
            if current is None:
                print("Index out of bounds")
                return
            current = current.next

        # if current is None:
        #     print("Index out of bounds")
        #     return

        new_node.next = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print()


llist = LinkedList()
llist.insert_at_index(0, 10)
llist.insert_at_index(1, 20)
llist.insert_at_index(1, 15)
llist.insert_at_index(3, 30)
llist.insert_at_index(2, 987)
llist.print_list()
