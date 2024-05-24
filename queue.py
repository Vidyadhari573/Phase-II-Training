#LinkedList Implementation of queue

class Box:
    def __init__(self, data):
        self.data = data 
        self.next = None
 
def printLinkedList(curr):
    if curr == None:
        print("Empty Linked list")
        return
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.next 
    print()
 
def enQueue(head, ele):
    temp = Box(ele) 
    if head == None:
        return temp
    tail = head 
 
    while tail.next != None:
        tail = tail.next 
    tail.next = temp
    return head 

def deQueue(head):
    if head == None:
	    return None 
    secondNode = head.next 
    head.next = None 
    return secondNode
 
queueHead = None 
printLinkedList(queueHead)
queueHead = enQueue(queueHead, 34)
queueHead = enQueue(queueHead, 35)
queueHead = enQueue(queueHead, 36)
queueHead = enQueue(queueHead, 37)
printLinkedList(queueHead)
queueHead = deQueue(queueHead)
printLinkedList(queueHead)
queueHead = deQueue(queueHead)
printLinkedList(queueHead)

#Array Implementation of queue

def enQueue(Q, ele):
    Q.append(ele)
    print(ele, " enqueued successfully")
 
 
def deQueue(Q):
    if len(Q) == 0:
        print("Queue is empty")
        return
    print(Q[0], " element is getting deleted")
    Q.pop(0)
 
Q = []
enQueue(Q, 10)
enQueue(Q, 20)
enQueue(Q, 30)
enQueue(Q, 40)
print(Q)
 
deQueue(Q)
print(Q)
 
deQueue(Q)
print(Q)
 
deQueue(Q)
print(Q)
 
deQueue(Q)
print(Q)
 
deQueue(Q)
print(Q)
