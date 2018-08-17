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

    def AtBegining(self, newdata):
        NewNode = Node(newdata)

        NewNode.nextval = self.headval
        self.headval = NewNode

    #insert after specific node
    def InBetween(self, middle_node, newdata):
        if middle_node is None:
            print('The node is empty')
            return

        NewNode = Node(newdata)
        #insert after B - make NewNode.next point to B.nextval
        #A - B - C => A - B - NewNode - C
        # NewNode = middle_node.nextval = C
        NewNode.nextval = middle_node.nextval
        #TWO POSITION CHANGES B -> NewNode -> B.nextval
        #B = NewNode
        middle_node.nextval = NewNode

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        #check if list is empty
        if self.headval is None:
            self.headval = NewNode
            return
        #traverse thru list
        laste = self.headval
        #keep checking if node has a next value
        while laste.nextval:
            laste = laste.nextval
        laste.nextval = NewNode

    def RemoveNode(self, RemoveKey):
        #Look for first item in list
        HeadVal = self.head
        #-- Delete head if removekey is first node --
        #Check to see if list is not empty
        if HeadVal is not None:
            #head value matches the removekey
            if HeadVal.data == RemoveKey:
                #A - B - C
                #B - C
                self.head = HeadVal.next
                #A = None
                HeadVal = None
                return

        #Keep checking for HeadVal
        while HeadVal is not None:

            if HeadVal.data == RemoveKey:
                break

            #A - B - C
            #prev = A - B - C
            prev = HeadVal
            #B - C
            HeadVal = HeadVal.next

        if HeadVal == None:
            return
        #prev.next = A 
        #headval.next = B
        prev.next = HeadVal.next

        HeadVal = None

list1 = LinkedList()
#print(list1)
list1.headval = Node('Mon')
#print(list1)
e2 = Node('Tue')
e3 = Node('Wed')

list1.headval.nextval = e2

e2.nextval = e3
list1.AtBegining('Sun')
list1.AtEnd('Sat')
list1.InBetween(list1.headval.nextval.nextval.nextval,'Thu')

list1.RemoveNode('Sat')

list1.listprint()
