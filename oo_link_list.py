class Node:
    """ Define a single node that holds a value and that can point to another 
        node."""
    
    def __init__(self):
        self.value = None
        self.next_node = None


class LinkedList:

    def __str__(self):
        """ Traverses a linked list and makes a string out of the values in each
            node."""
        
        a_string = str(self.head.value)
        
        #Get ready to traverse the list while we have a non-empty next node
        current_node = self.head.next_node
        while current_node:

            a_string = a_string + " " + str(current_node.value)
            #Move the pointer ahead
            current_node = current_node.next_node

        return a_string

    def __init__(self):

        self.head = Node()

    def search(self, a_value):
        """ Return the first node in the list with a_value."""
        
        #Base case is the value in the head?
        if self.head.value == a_value:
            return self.head

        #Get ready to traverse the list & return the first node with the value.
        examined_node = self.head.next_node
        while examined_node:

            if examined_node.value == a_value:
                
                return examined_node

            else: 
                #We didn't find the value so move on to next pointer
                examined_node = examined_node.next_node

        #We didn't find the value anywhere. So return none.
        return None

    def add(self, a_value):
        
        # If the head has a value move on
        if self.head.value:

            # If even though the head has a value but no other nodes
            if self.head.next_node == None:
                
                # Make a new node to put the value in.
                self.head.next_node = Node()
                self.head.next_node.value = a_value

        
            #The head has a value and it points to other non-empty nodes.
            else:
                
                #Begin looping through the linked list to the end
                examined_node = self.head.next_node
                while examined_node.next_node != None:
                    #Move the pointer to the next node.
                    examined_node = examined_node.next_node

                #Make a new node at the end
                examined_node.next_node = Node() 
                examined_node.next_node.value = a_value
        else:
            # The head didn't have a value yet so it gets the value.
            self.head.value = a_value

    def remove(self, a_value):
        """Remove a node by redirecting the branch of the linked list around it
        after finding the first node with  a_value. FURTHER REFINEMENT
         NECESSARRY TO HANDLE ALL CASES I BELIEVE."""
        
        nodes_to_trim = self.remove_helper(a_value)

        if nodes_to_trim == "Value not found.":
            return nodes_to_trim

        # in  the case where the value was found in the head of a non-empty list
        if not nodes_to_trim[0] and nodes_to_trim[1].next_node:
        
            self.head = nodes_to_trim[1].next_node

        else:
            nodes_to_trim[0].next_node = nodes_to_trim[1].next_node 
             


    def remove_helper(self, a_value):
        """Almost identical to serach. We should go back and implement this with inheritance?"""
          #Base case is the value in the head?
        if self.head.value == a_value:
            return (None, self.head)

        #Get ready to traverse the list & return the first node with value.
        last_examined_node = None
        examined_node = self.head.next_node
        while examined_node:

            if examined_node.value == a_value:
                return (last_examined_node, examined_node)

            else: 
                #We didn't find the value so move on to next pointer
                last_examined_node = examined_node
                examined_node = examined_node.next_node

        #We didn't find the value anywhere. So return none.
        return "Value not found."



def main():

    """y = LinkedList()
    y.add('a')
    y.add('b')
    y.add('c')
    print(y.head.value)
    print(y)"""

    link = LinkedList()
    link.add(4)
    link.add(2)
    link.add(86)
    link.add(4)
    link.add(7)
    print("Current list:", link)
    link.remove(4)
    print("List after first 4 is removed:", link)
    link.remove(4)
    print("List after second 4 is removed:", link)
    print("Success! Attempt to remove a third 4 yielded no crashes!")
    link.remove(4)

   


   

   # Output of above code:

   # -------------------------

   # Current list: 4 2 86 4 7 

   # List after first 4 is removed: 2 86 4 7 

   # List after second 4 is removed: 2 86 7 

   # Attempt to remove a third 4 yielded no crashes



main()