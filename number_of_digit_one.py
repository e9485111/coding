import math
def findlog(num):
  c = 0
  while num:
    c+=1
    num /= 10
    print num
  return c-1
class Solution:
  # @param {integer} n
  # @return {integer}
  def countDigitOne(self, n):
    if n < 0:
      return 0
    return self.helper(abs(n))

  def helper(self, num):
    if num == 0:
      return 0
    if num >= 1 and num <=9:
      return 1
    p = findlog(num)
    order = pow(10,p)
    highest = num/order
    print highest, order, num, num/order, p
    if highest == 1:
      return self.helper(order-1) + 1 + num % order + self.helper(num % order)
    else:
      return order + highest * self.helper(order-1) + self.helper(num % order)




s = Solution()
print s.countDigitOne(1000)

