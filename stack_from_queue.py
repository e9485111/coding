from collections import deque
class Stack:
    # initialize your data structure here.
    def __init__(self):
       self.q1=deque()
       self.q2=deque()

    # @param x, an integer
    # @return nothing
    def push(self, x):
        if self.q1:
          self.q1.append(x)
        else:
          self.q2.append(x)

    # @return nothing
    def pop(self):
      if self.q1 and not self.q2:
        first = self.q1
        second = self.q2
      elif self.q2 and not self.q1:
        first = self.q2
        second = self.q1
      else:
        return None

      while len(first) > 1:
        second.append(first.popleft())
      return first.popleft()

    # @return an integer
    def top(self):
      if self.q1 and not self.q2:
        first = self.q1
        second = self.q2
      elif self.q2 and not self.q1:
        first = self.q2
        second = self.q1
      else:
        return None

      while len(first) > 1:
        second.append(first.popleft())
      v = first.popleft()
      second.append(v)
      return v

    # @return an boolean
    def empty(self):
        if not self.q1 and not self.q2:
            return True
        return False
s = Stack()
s.push(1)
s.push(2)
print s.top()
s.push(3)
print s.top()
