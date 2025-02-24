class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class circular_ll:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)

        if (not self.head):
            new_node.next = new_node
            self.head = new_node
            return

        # traverse to the last node
        curr = self.head
        while (curr.next != self.head):
            curr = curr.next

        curr.next = new_node
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)

        if (not self.head):
            new_node.next = new_node
            self.head = new_node
            return

         # traverse to the last node
        curr = self.head
        while (curr.next != self.head):
            curr = curr.next

        curr.next = new_node
        new_node.next = self.head

    def insert_at_index(self, indx, data):
        if indx == 0:
            self.prepend(data)
            return

        temp = self.head
        for i in range(indx-1):
            temp = temp.next
            if (temp == self.head):
                print("index out of bounds")
                return

        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node

    def del_at_beginning(self):
        curr = self.head

        if self.head:
            while curr.next != self.head:
                curr = curr.next

            curr.next = self.head.next
            self.head = curr.next

    def del_at_end(self):
        curr = self.head

        if self.head:
            while curr.next.next != self.head:
                curr = curr.next

            curr.next = self.head

    def del_at_indx(self, indx):
        curr = self.head

        if (indx == 0):
            self.del_at_beginning()
            return

        if self.head:
            while curr.next.next != self.head:
                curr = curr.next

            curr.next = curr.next.next

    def print(self):
        temp = self.head

        while True:
            print(temp.data, end="->")
            temp = temp.next
            if (temp == self.head):
                break
        print()


dll = circular_ll()
for i in range(101, 110):
    dll.append(i)

dll.print()
dll.insert_at_index(9, 15)
dll.print()
dll.del_at_indx(9)
dll.print()

# dll.insert(1, 80)
