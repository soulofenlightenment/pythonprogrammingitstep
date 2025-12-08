#linked list(singly)
"""
Demo version of this module
// i will update it and make more efficent and stable 

requirement of class node(
    node is storage that stores: data and pointer(that points to the next node)
)
initialize(node) - inserting first node(prepearing list); head -> n_1
insert_f(node) - adding node at the end
insert_l(node) - adding node to a start
del_node(node) - deleting node without breaking a list chain
search(node) - telling where our node lies beetween
traverse() - display list
link(attach, node) - adding new node after node which is in the list
void() - returns true if there is no node in the list(if list empty)
reverse() - reverse list
length() - amount of nodes in the list
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None

    def initialize(self,new_head):
        if self.head == None:
            self.head = new_head
        else:
            return 'list is already initialized'
    
    def insert_f(self,node):
        node.next = self.head
        self.head = node

    def insert_l(self,node):
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = node
    
    def del_node(self,node):
        current_node = self.head
        prev = None
        while current_node:
            if current_node.data == node.data:
                if prev == None:
                    self.head = current_node.next
                else:
                    prev.next = current_node.next
                break
            else:
                prev = current_node
                current_node = current_node.next

    def search(self,node):
        current_node = self.head
        prev = None
        while current_node:
            if current_node.data == node.data:
                back = prev.data if prev else "None"
                forward = current_node.next.data if current_node.next else "None"
                return f'{back} --> {current_node.data} --> {forward}'
            else:
                prev = current_node
                current_node = current_node.next

    def traverse(self):
        current_node = self.head
        path = "None --> " 
        if self.head:  
            while current_node:
                path += str(current_node.data) + " --> "
                current_node = current_node.next
            path += "None"       
            return path
        else:
            return 'None'

    def link(self,attach,node):
        pass
        #not inplemented yet


    def void(self):
        if self.head == None:
            return True
        else:
            return False
    
    def reverse(self):
        #not inplemented yet
        pass
    def length(self):
        pass
    #not inplemented yet

ll = LinkedList()
ll.initialize(Node(5))
ll.insert_f(Node(10))
ll.insert_f(Node(7))
ll.insert_f(Node(9))
ll.insert_f(Node(1))
print(ll.traverse())
print(ll.traverse())
        
    
                




            




