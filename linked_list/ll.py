# Definition for singly-linked list node
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

# Function to reverse the linked list
def reverseLinkedList(head: Node) -> Node:
    prev = None
    current = head
    while current:
        next_node = current.next  # Save the next node
        current.next = prev  # Reverse the link
        prev = current  # Move prev to current node
        current = next_node  # Move to the next node
    return prev  # prev will be the new head of the reversed list

# Function to print the linked list (for testing purposes)
def printLinkedList(head: Node) -> None:
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Create a linked list for testing
head = Node(2)
second = Node(4)
third = Node(3)


# Linking nodes
head.next = second
second.next = third



head2 = Node(5)
second2 = Node(6)
third3 = Node(4)


head2.next = second2
second2.next = third3


reversed_head1 =  reverseLinkedList(head)
reversed_head2 = reverseLinkedList(head2)

printLinkedList(reversed_head1)
printLinkedList(reversed_head2)

arr1 = []
arr2 = []

temp = reversed_head1
temp2 = reversed_head2

while temp:
    arr1.append(temp.data)
    temp = temp.next

while temp2:
    arr2.append(temp2.data)
    temp2 = temp2.next

print(arr1,arr2)

str1=""
str2=""

for i in arr1:
    str1+=str(i)
for j in arr2:
    str2+=str(j)
    
print(str1,str2," ",int(str1)+int(str2))

# # Print the original linked list
# print("Original Linked List:")
# printLinkedList(head)

# # Reverse the linked list
# reversed_head = reverseLinkedList(head)

# # Print the reversed linked list
# print("Reversed Linked List:")
# printLinkedList(reversed_head)
