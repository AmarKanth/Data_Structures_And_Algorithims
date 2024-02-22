"""
It is same as single linked list, last node stores the first node reference.
       10-->20-->30-->40-->None
None<--10<--20<--30<--40
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def create(self, value):
        new_node = Node(value)
        new_node.next = None
        new_node.prev = None
        self.head = new_node
        self.tail = new_node
        return 'DLL created'
    
    def insert(self, value, location):
        new_node = Node(value)

        if self.head == None:
            return "DLL is not exist"
        else:
            if location == 0:
                new_node.prev = None
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            elif location == -1:
                new_node.next = None
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                new_node.next = temp_node.next
                new_node.prev = temp_node
                new_node.next.prev = new_node
                temp_node.next = new_node
        
    def traverse(self):
        if self.head is None:
            return "DLL is not exist"
        temp_node = self.head
        while temp_node:
            print(temp_node.value)
            temp_node = temp_node.next
    
    def reverse_traverse(self):
        if self.head is None:
            return "DLL is not exist"
        temp_node = self.tail
        while temp_node:
            print(temp_node.value)
            temp_node = temp_node.prev
    
    def search(self, value):
        if self.head is None:
            return "DLL is nto exist"
        temp_node = self.tail
        while temp_node:
            if temp_node.value == value:
                return temp_node.value
            temp_node = temp_node.next
        return "value is not exist in the DLL"
    
    def delete(self, location):
        if self.head is None:
            return "DLL is not exist"
        
        if location == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        
        if location == -1:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
        
        if location not in [0,-1]:
            current_node = self.head
            index = 0
            while index < location -1:
                current_node = current_node.next
                index += 1
            current_node.next = current_node.next.next
            current_node.next.prev = current_node
            return "Element is deleted successfully"
    
    def delete(self):
        if self.head is None:
            return "DLL is not exist"
        
        temp_node = self.head
        while temp_node:
            temp_node.prev = None
            temp_node = temp_node.next
        self.head = None
        self.tail = None
        return "DLL is successfully deleted"

q = DoubleLinkedList()
print(q.create(5))
print([i.value for i in q])