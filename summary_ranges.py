class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        start = None
        last = None
        end = None
        ret = []
        for i in range(0,len(nums)):
          val = nums[i]
          if start is None:
            start = val
            last = start
          else:
            if val == last+1:
              last = val
            else:
              if start != last:
                ret.append("%s->%s" % (start, last))
              else:
                ret.append("%s" % start)
              start = val
              last = val

        if start is not None:
          if start != last:
            ret.append("%s->%s" % (start, last))
          else:
            ret.append("%s" % start)
        return ret

s = Solution()
#print s.summaryRanges([0,1,2,4,5,7])
#print s.summaryRanges([0])
print s.summaryRanges([0,1])
#print s.summaryRanges([])


