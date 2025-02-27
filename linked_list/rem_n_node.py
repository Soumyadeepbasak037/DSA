class Node:
    def __init__(self,data,next=None) -> None:
        self.data = data
        self.next = next
    
head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)

head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = None

def print_list(head):
    temp = head
    while temp:
        print(temp.data,end="->")
        temp = temp.next


def reverse_list(head:Node):
    cur = head
    prev = None
    while cur:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
    return prev

        

def rem_n_node(head:Node,n):
    ctr = 0
    temp = head
    while temp:
        if(ctr==n-2):
            temp_prev = temp
            temp_cur = temp.next
            temp.next = temp_cur.next
            print(temp.data)
            print(temp.next.data)
            
        ctr+=1
        temp = temp.next
    
    
    

# print_list(head)
reversed_head = reverse_list(head)
rem_n_node(reversed_head,3)
print_list(reversed_head)
