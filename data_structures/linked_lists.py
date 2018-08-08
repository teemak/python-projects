class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class LinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

list1 = LinkedList()
print(list1)
list1.headval = Node('Mon')
print(list1)
e2 = 'Tue'
e3 = 'Wed'

list1.headval.nextval = e2

#e2.nextval = e3
list1.listprint()
