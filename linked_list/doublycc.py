class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            tail = self.head.prev
            new_node.next = self.head
            new_node.prev = tail
            tail.next = new_node
            self.head.prev = new_node
            self.head = new_node

    def insert_at_index(self, index, data):
        if index == 0:
            self.prepend(data)
            return
        new_node = Node(data)
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
            if temp == self.head:
                return  # Index out of bounds
        new_node.next = temp.next
        new_node.prev = temp
        temp.next.prev = new_node
        temp.next = new_node

    def display(self):
        if not self.head:
            return
        temp = self.head
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print()

