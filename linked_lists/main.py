# diff between list and linked list
# linked list - no index
# list -continguous in memory
# linked list - spread about memory
# ll - variable called head points to first item, tail points to last item, each node points to next item in list
# ll - Big O
# append to end - last node point to new item and move tail to the new item - 0(1) - no matter how many items in the list the number of operations to add to the end of the list is the same
# remove from end - to move tail we have to find the node that pointed to the item that is removed so we have to iterate through the list until we get to the node that pointed to the removed item, then we can set tail to that node - O(n) - because we had to iterate through the whole list
# add to the front - have to move the head, point the new item to the previous first item and point the head at the new item - O(1) - same number of operations no matter how many items in the list
# remove from the front - have head point to the new next, remove the item, still O(1) - same number of operations no matter how many items in the list
# add item in the middle of the list - have to iterate in the list until we get to the place we want to insert, have to set the new node to point to the next node and have to set the previous node to point to the new node - because we have to iterate through the list it is O(n)
# remove item from the middle of the list - have to iterate in teh list until we get to the item we want to remove, have to set the previous node to the new next node - because we hve to iterate through the list so O(n)
# lookup for linked list - have to iterate through the list until we find the item we want, O(n), with a normal list we can look up by index so O(1) but with a linked list since there is no index we have to iterate and so its O(n)
# A node is made up from a value and a pointer, you can think of a node as a dictorary with a value and a next of None when its at the end

# thinking about it as a set of nested dictionaries
head = {
    "value": 11,
    "next": {
        "value": 3,
        "next": {
            "value": 23,
            "next": {
                "value": 7,
                "next": None
            }
        }
    }
}

print(head['next']['next']['value'])

# ll constructor
class LinkedList:
    def __init__(self, value):
        # create new Node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        # create new node, add node to end
        pass

    def prepend(self, value):
        # create new node, add node to beg
        pass
    
    def insert(self, index, value):
        # create new node, add node at index
        pass

# to prevent having to write code to create a new node 4 times, we should write a class to create nodes


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

my_linked_list = LinkedList(4)

print(my_linked_list.head.value)
