class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value
    
    def get_next_node(self):
        return self.next_node
    
    def set_next_node(self, node):
        self.next_node = node

class LinkedList:
    def __init__(self, value = None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node
    
    def insert_beginning(self, value):
        self.head_node = Node(value, self.head_node)

    def stringify_list(self, prev_string = '', prev_node = None):
        working_node = prev_node if prev_node is not None else self.head_node
        working_string = prev_string + str(working_node.get_value())
        
        if working_node.get_next_node() is None:
            print("Here")
            print(working_string)
            return working_string

        # Only runs when not last element in tree, should pass current data to next run of function
        if working_node.get_next_node() is not None:
            self.stringify_list(working_string + "\n", working_node.get_next_node())
        

ll = LinkedList("string")
ll.insert_beginning("string2")
this_will_be_info = ll.stringify_list()
print(this_will_be_info)