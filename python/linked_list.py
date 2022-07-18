class LinkList:
  # write your __init__ method here that should store a 'head' value which the first Node in the LinkedList and a 'length' value which is the total number of Nodes in the LinkedList
  def __init__(self):
    self.linked_list = []
    self.head = self.linked_list[0]
    self.length = len(self.linked_list)

  def add(self, data):
    # write your code to ADD an element to the Linked List
    self.linked_list.append(data) 

  def remove(self, data):
    # write your code to REMOVE an element from the Linked List
    self.linked_list.removed(data)

  def get(self, element_to_get):
    # write you code to GET and return an element from the Linked List
    return self.linked_list[element_to_get]

# ----- Node ------
class Node:
  # store your DATA and NEXT values here
  pass
