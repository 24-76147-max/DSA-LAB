# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create first node
node1 = Node('Buksan mo by Willie Revillame')
head = node1


# Traverse
def traverseLinkedList():
    current = head
    while(current):
        print(current.data, end=" -> ")
        current = current.next
    print("None")


# Insert at Beginning
def insertNodeAtTheBeginning(data):
    global head
    newNode = Node(data)

    if(head == None):
        head = newNode
    else:
        newNode.next = head
        head = newNode


# Calls (Beginning)
insertNodeAtTheBeginning('Ale by the Bloomfields')
insertNodeAtTheBeginning('Lifetime by Ben&Ben')
insertNodeAtTheBeginning('Mundo IV of Spades')

traverseLinkedList()


# Insert at End
def insertNodeAtTheEnd(data):
    global head
    newNode = Node(data)

    if(head == None):
        head = newNode
    else:
        current = head
        while(current.next != None):
            current = current.next
        current.next = newNode


# Calls (End)
insertNodeAtTheEnd('Leaves by Ben&Ben')
insertNodeAtTheEnd('Kathang Isip by Ben&Ben')


# Insert After Given Node (fixed but same style)
def insertNodeAfterGivenNode(data, node):
    global head
    newNode = Node(data)

    if(head == None):
        head = newNode
    else:
        current = head

        # find the node
        while(current != None and current.data != node):
            current = current.next

        if(current == None):
            print('The node does not exist')
            return

        newNode.next = current.next
        current.next = newNode


# Calls (Middle)
insertNodeAfterGivenNode('Ikaw', 'Lifetime by Ben&Ben')
insertNodeAfterGivenNode('Buwan', 'Leaves by Ben&Ben')


# Final Output
traverseLinkedList()
