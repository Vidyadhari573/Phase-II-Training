
class Box:
    def __init__(self, data):
        self.data = data
        self.next = None
def printLinkedList(curr):
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.next
    print()
'''obj1 = Box(51)
obj2 = Box(52)
obj3 = Box(53)
obj4 = Box(54)
obj5 = Box(55)
obj6 = Box(56)
obj7 = Box(57)
obj8 = Box(58)
obj9 = Box(59)
obj10 = Box(60)


obj1.next = obj2
obj2.next = obj3
obj3.next = obj4
obj4.next = obj5
obj5.next = obj6
obj6.next = obj7
obj7.next = obj8
obj8.next = obj9
obj9.next = obj10
obj10.next = None'''
'''printLinkedList(obj4)
print(obj2.data,obj2)
print(obj3.data,obj3)
print(obj4.data,obj4)
print(obj5.data,obj5)
print(obj6.data,obj6)
print(obj7.data,obj7)
print(obj8.data,obj8.next)
print(obj9.data,obj9.next)
print(obj10.data,obj10.next)'''

'''def InsertAtTailNode(head,ele):
    temp = Box(ele)
    if head == None:
        return temp
    tail = head
    while tail.next != None:
        tail = tail.next
    tail.next = temp
    return head
head = None
nums = [10,20,30,40,50,60,70,80,90,100]
for ele in nums:
    head = InsertAtTailNode(head, ele)
printLinkedList(head)

def InsertAtBeginning(head,ele):
    temp = Box(ele)
    if head == None:
        return temp
    temp.next = head
    return temp
head = None
nums = [10,20,30,40,50,60,70,80,90,100]
for ele in nums:
    head = InsertAtBeginning(head, ele)
printLinkedList(head)

def insertAtSpecificPosition(head, position, ele):
    if position == 0:
        return InsertAtBeginning(head, ele)
 
    temp = Box(ele)
    currentIndex = 0 
    currentNode = head 
    while currentIndex != position - 1:
        currentIndex += 1 
        currentNode = currentNode.next 
    temp.next = currentNode.next 
    currentNode.next = temp 
    return head'''
 
'''head = None
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for ele in nums:
    head = InsertAtBeginning(head, ele)
head = insertAtSpecificPosition(head, 5, 1899)
printLinkedList(head)'''

def DeleteAtHead(head):
    if head == None:
        return None
    secondnode = head.next
    head.next = None
    return secondnode

head = None
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
printLinkedList(head)
for ele in nums:
    head = DeleteAtHead(head)
printLinkedList(head)