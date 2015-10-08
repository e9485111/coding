class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
      op = 1
      val = 1
      arr = []
      if numRows == 1:
        return s
      for i in s:
        arr.append((val, i))
        if val == numRows:
          op = -1
        elif val== 1:
          op = 1
        val += op
      arr = sorted(arr, key=lambda x : x[0])
      print arr
      ret = ""
      for i in arr:
        ret += i[1]
      return ret
s = Solution()
print s.convert("AB", 1)
#print s.convert("PAYPALISHIRING", 3)
#print s.convert("", 3)
#print s.convert("PAHNAPLSIIGYIR", 2)
