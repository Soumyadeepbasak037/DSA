class node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next


head = node(1)
second = node(1)
third = node(2)
fourth = node(3)
fifth = node(3)

head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = None

current = head
while current and current.next:
    if current.data == current.next.data:
        current.next = current.next.next
    else:
        current = current.next
