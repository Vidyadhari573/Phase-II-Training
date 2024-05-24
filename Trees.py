class Box:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
def printInOrderTraversal(root):
    if root == None:
        return
    printInOrderTraversal(root.left)
    print(root.data, end = " ")
    printInOrderTraversal(root.right)

def printPreOrderTraversal(root):
    if root == None:
        return
    print(root.data, end = " ")
    printPreOrderTraversal(root.left)
    printPreOrderTraversal(root.right)
    
def printPostOrderTraversal(root):
    if root == None:
        return
    printPostOrderTraversal(root.left)
    printPostOrderTraversal(root.right)
    print(root.data, end = " ")
    
def levelOrderTraversal(root):
    if root == None:
        return 
    result = []
    Q = [root]
 
    while len(Q) > 0:
        n = len(Q)
        subResult = []
        for i in range(n):
            # step - 1
            currNode = Q.pop(0)
 
            # step - 2
            subResult.append(currNode.data)
 
            # step - 3
            if currNode.left != None:
                Q.append(currNode.left)
 
            # step - 4
            if currNode.right != None:
                Q.append(currNode.right)
 
        result.append(subResult)
 
    print(result)
            


obj1 = Box(-105)
obj2 = Box(1)
obj3 = Box(82)
obj4 = Box(28)
obj5 = Box(-15)
obj6 = Box(-18)
obj7 = Box(27)
obj8 = Box(22)

obj1.left = obj2
obj1.right = obj3
obj2.right = obj4
obj4.left = obj7
obj3.left = obj5
obj5.left = obj6
obj5.right = obj8

levelOrderTraversal(obj1)

    
    
        