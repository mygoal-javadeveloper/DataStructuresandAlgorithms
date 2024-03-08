class Node():
    def __init__(self, k):
        self.key = k
        self.next = None

def search(head, x):
    pos=1
    curr=head
    while curr != None:
        if curr.key == x:
            return pos
        pos += 1
        curr = curr.next
    return -1


head = Node(10)
head.next = Node(15)
head.next.next = Node(20)
head.next.next.next = Node(25)
x = 20
print(search(head, x))
print(search(head, 110))
