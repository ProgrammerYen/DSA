from platform import node


class Node:
    
    def __init__(self, data):
        self.next = None
        self.data = data
    
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    
    def push(self, val):
        # appends a new value to a linked list
        if self.head == None:
            self.head = Node(val)
            
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
                
            curr.next = Node(val)
            
            
    def show_llist(self):
        # presents the linked list values
        curr = self.head
        llist = []
        while curr != None:
            llist.append(curr.data)
            curr = curr.next
        
        return llist
            
    
    def length_llist(self):
        # finds the length of the linked list
        curr = self.head
        count = 0
        while curr != None:
            curr = curr.next
            count += 1
            
        return count
    
    
    def get_element_pos(self, element):
        # returns the index of an element in the linked list
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
        

    def swap_two_vals(self, val1, val2):
        # swaps the position of two values in the linked list
        pos1 = self.get_element_pos(val1)
        pos2 = self.get_element_pos(val2)
        
        curr = self.head
        count = 0
        while curr != None:
            if count == pos1:
                curr.data = val2 
                
            elif count == pos2:
                curr.data = val1
                
            curr = curr.next
            count += 1 
            
            
linked_list1 = LinkedList()
linked_list1.push(2)
linked_list1.push(5)
linked_list1.push(1)
linked_list1.push(12)
linked_list1.push(13)

print(linked_list1.show_llist())
linked_list1.reverse()
print(linked_list1.show_llist())

print(linked_list1.get_element_pos(1))

print(linked_list1.length_llist())

linked_list1.swap_two_vals(2,5)
print(linked_list1.show_llist())