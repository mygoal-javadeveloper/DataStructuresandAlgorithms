class Node():
    def __init__(self, k):
        self.key = k
        self.next = None


def printlinkedlist(head):
    curr = head
    while curr is not None:
        print(curr.key, end = ' ')
        curr = curr.next
    print()

def printmiddle(ptr):
    if head == None:
        return
    count = 0
    curr = head
    while curr:
        count += 1
        curr = curr.next
    curr = head
    for x in range(count//2):
        curr = curr.next
    print(curr.key)







head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
printlinkedlist(head)
printmiddle(head)