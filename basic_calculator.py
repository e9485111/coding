import re
class Solution:
    # @param {string} s
    # @return {integer}

    def __init__(self):
      self.index = 0
    def calculate(self, s):
      s = re.sub('\s', '', s)
      return self.calc(s)
    def calc(self, s):
      val = 0
      curr_sign = 1
      curr_val = 0
      while self.index < len(s):
        char = s[self.index]
        self.index += 1
        if char == '(':
          v = self.calc(s)
          val += curr_sign*v
        elif char == ')':
          return val+curr_sign*curr_val
        elif char == '+':
          val += curr_sign*curr_val
          curr_val = 0
          curr_sign = 1
        elif char == '-':
          val += curr_sign*curr_val
          curr_val = 0
          curr_sign = -1
        else:
          curr_val = curr_val*10+int(char)
      if curr_val:
        val += curr_sign*curr_val

      return val

s=Solution()
print s.calculate(" 2-1 + 2 ")


