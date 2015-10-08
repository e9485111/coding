class Solution(object):
  def fractionToDecimal(self, numerator, denominator):
    """
    :type numerator: int
    :type denominator: int
    :rtype: str
    """
    sign = 1
    if numerator < 0:
      numerator *= -1
      sign *= -1
    if denominator < 0:
      denominator *= -1
      sign *= -1

    q = numerator / denominator
    r = numerator % denominator
    res = self.helper(r*10, denominator, [], [])
    res = [str(i) for i in res]
    if res:
      if sign == 1:
        return "%s.%s" % (q,"".join(res))
      else:
        return "-%s.%s" % (q,"".join(res))
    else:
      return str(q*sign)

  def helper(self, num, denom, fnum, results):
    #print num, denom, fnum, results
    if num == 0:
      return results
    if num in fnum:
      ind = fnum.index(num)
      results.insert(ind, "(")
      results.append(")")
      return results
    else:
      fnum += [num]
    q = num / denom
    r = num % denom
    results += [q]
    return self.helper(r*10, denom, fnum, results)

s = Solution()
print s.fractionToDecimal(-50,8)
print s.fractionToDecimal(0,3)
print s.fractionToDecimal(2,1)
print s.fractionToDecimal(3,10)
print s.fractionToDecimal(5,12)
print s.fractionToDecimal(22,7)
print s.fractionToDecimal(2,3)
print s.fractionToDecimal(1,81)
print s.fractionToDecimal(9,11)
print s.fractionToDecimal(1,9)
print s.fractionToDecimal(2,3)

