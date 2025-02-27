class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class doubly_ll:

    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, data):
        new_node = node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def append(self, data):  # wrong
        new_node = node(data)

        if not self.tail:
            self.head = new_node
            self.tail = new_node
            return

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def insert(self, data, indx):
        if indx == 0:
            self.prepend(data)
            return

        temp = self.head
        for i in range(indx):
            temp = temp.next
            if not temp:
                print("Invalid indx")
                return

        if temp == self.tail:
            self.append(data)
            return

        new_node = node(data)
        new_node.next = temp.next
        temp.next.prev = new_node
        new_node.prev = temp.prev
        temp.prev.next = new_node

    def print_fwd(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print()

    def print_bkd(self):
        temp = self.tail
        while temp:
            print(temp.data, end="<-")
            temp = temp.prev
        print()

    def deleteFromBegining(self):
        if (self.head):
            self.head = self.head.next
            self.head.prev = None

    def deleteFromEnd(self):
        if (self.tail):
            self.tail = self.tail.prev
            self.tail.next = None

    def deleteAtIndx(self, indx):
        if indx == 0:
            self.deleteFromBegining()
            return

        temp = self.head
        for i in range(indx):
            temp = temp.next
            if not temp:
                print("Invalid indx")
                return

        if temp == self.tail:
            self.deleteFromEnd()
            return

        temp.prev.next = temp.next
        temp.next.prev = temp.prev


dll = doubly_ll()
for i in range(101, 110):
    dll.append(i)

dll.print_fwd()
dll.print_bkd()

# dll.insert(1, 80)
dll.deleteAtIndx(6)
dll.print_fwd()
dll.print_bkd()
