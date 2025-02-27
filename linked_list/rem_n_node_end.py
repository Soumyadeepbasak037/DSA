class node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = node(1)
head.next = node(2)
head.next.next = node(3)
head.next.next.next = node(4)


def ll_len(head: node):
    temp = head
    count = 0
    while (temp):
        # print(temp.data, end="->")
        temp = temp.next
        count += 1
    print(count)


ll_len(head)
req_len =
