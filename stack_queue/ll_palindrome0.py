class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


head = node(1)
head.next = node(2)
head.next.next = node(2)
head.next.next.next = node(1)
# head.next.next.next.next = node(5)

temp = head
stack = []
while temp:
    stack.append(temp.data)
    temp = temp.next

cp_stack = stack.copy()
res = []

for i in range(len(stack)):
    res.append(stack.pop())

print(cp_stack == res)
