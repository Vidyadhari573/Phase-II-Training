# LinkedList Implementation of Stack

class Box:
    def __init__(self, data):
        self.data = data 
        self.next = None
 
def printStack(curr):
    if curr == None:
        print("Stack is empty")
        return 
 
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.next 
    print()
 
def pop(head):
    if head == None:
	    return None 
    print(head.data, "deleted successfully")
    secondNode = head.next 
    head.next = None 
    return secondNode 
 
def push(head, ele):
    print(ele, " inserted successfully")
    temp = Box(ele)
    if head == None:
        return temp 
    temp.next = head 
    return temp
 
head = None 
head = push(head, 10)
head = push(head, 20)
head = push(head, 30)
head = push(head, 40)
printStack(head)
 
head = pop(head)
printStack(head)
 
head = pop(head)
printStack(head)
 
head = pop(head)
printStack(head)
 
head = pop(head)
printStack(head)
 
head = pop(head)
printStack(head)

# Array Implementation of Stack

def push(stack, ele):
    stack.insert(0, ele)
    print(ele, " inserted into stack successfully")
 
def pop(stack):
    if len(stack) == 0:
        print("stack is empty")
        return 
    print(stack[0], "deleted successfully")
    stack.pop(0)
 
stack = []
push(stack, 10)
push(stack, 20)
push(stack, 30)
push(stack, 40)
push(stack, 50)
print(stack)
 
pop(stack)
print(stack)
 
pop(stack)
print(stack)
 
pop(stack)
print(stack)
 
pop(stack)
print(stack)
 
pop(stack)
print(stack)
 
pop(stack)
