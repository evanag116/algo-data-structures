class Stack:
  # write your __init__ method here that should store a 'total' value which is the total number of elements in the Stack and a 'stack' value which is an array of stored values in the Stack

  def __init__(self):
    self.stack = []
    total = len(self.stack)

  def push(self, data):
    # write your code to add data following LIFO and return the Stack
    self.stack.append(data)

  def pop(self):
    # write your code to removes the data following LIFO and return the Stack
    self.stack.remove(self.stack[-1])

  def size(self):
    # write your code that returns the size of the Stack
    return len(self.stack)



stack1 = Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)
stack1.pop()
print(stack1.size())
print(stack1.stack)


