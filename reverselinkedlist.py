class Node():
    def __init__(self, k):
        self.key = k
        self.next = None


def reverselinkedlist(head):
    stacklinkedlist = []
    curr = head
    while curr is not None:
        stacklinkedlist.append(curr.key)
        curr = curr.next
    curr = head
    while curr is not None:
        curr.key = stacklinkedlist.pop()
        curr = curr.next
    curr = head
    while curr is not None:
        print(curr.key, end = ' ')
        curr= curr.next






head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
reverselinkedlist(head)


