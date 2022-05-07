class Node:
    
    def __init__(self, data):
        self.next = None
        self.data = data
    
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    
    def push(self, val):
        """Adds a new value to a linked list"""
        if self.head == None:
            self.head = Node(val)
            
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
                
            curr.next = Node(val)
            
            
    def show_llist(self):
        """Presents the linked list values"""
        curr = self.head
        llist = []
        while curr != None:
            llist.append(curr.data)
            curr = curr.next
        
        return llist
            
    
    def length_llist(self):
        """Finds the length of the linked list"""
        curr = self.head
        count = 0
        while curr != None:
            curr = curr.next
            count += 1
            
        return count
    
    
    def get_element_pos(self, element):
        curr = self.head
        count = 0
        while curr != None:
            if curr.data == element:
                return count
            
            curr = curr.next
            count += 1
            
    
    def reverse(self):
        """Reverse the order of the values in a linked list"""
        # Firstly, we will create three pointers and the three pointers will be prev, curr, and nxt.
        # Then, we will move through the linked list, changing the direction of the pointers so that the curr pointer will 
        # be pointing to the prev pointer and the next pointer will be pointing to the curr pointer.
        # Finally, the head of the linked list should be the prev pointer.
        
        # a --> b --> c --> d --> None
        # Result: d --> c --> b --> a --> None
        
        prev, curr = None, self.head
        while curr != None:
            nxt = curr.next
            curr.next = prev
            
            prev = curr
            curr = nxt
            
        self.head = prev
        

linked_list1 = LinkedList()
linked_list1.push(2)
linked_list1.push(5)
linked_list1.push(1)

print(linked_list1.show_llist())
linked_list1.reverse()
print(linked_list1.show_llist())

print(linked_list1.get_element_pos(1))
print(linked_list1.length_llist())