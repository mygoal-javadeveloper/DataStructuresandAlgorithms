class Node():
    def __init__(self, k):
        self.key = k
        self.next = None


def reverselinkedlisteffectively(head):
    curr = head
    prev = None
    while curr is not None:
        next  = curr.next
        curr.next = prev
        prev = curr
        curr = next
    curr = prev
    while curr is not None:
        print(curr.key)
        curr = curr.next

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
reverselinkedlisteffectively(head)


