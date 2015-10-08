class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
      if nums and len(nums) <=2:
        if len(nums) == 2:
          if nums[0] == nums[1]:
            return [nums[0]]
        return nums
      ret = []
      v = self.run(nums)
      if v is not None:
        ret += [v]
        v1 = self.run(nums, [v])
        if v1 is not None:
          ret += [v1]
      return ret

    def run(self, nums, ignore = []):
      v1 = None
      v2 = None
      c1 = 0
      c2 = 0
      for i in nums:
        print v1, v2, c1, c2
        if i in ignore:
          continue
        if c1 == 0:
          v1 = i
          c1 = 1
        elif i == v1:
          c1 += 1
        elif c2 == 0:
          v2 = i
          c2 = 1
        elif i == v2:
          c2 += 1
        else:
          c1 -= 1
          c2 -= 1
      new_c1 = 0
      new_c2 = 0
      for i in nums:
        if i == v1:
          new_c1 += 1
        if i == v2:
          new_c2 += 1
      if new_c1 > len(nums)/3:
        return v1
      if new_c2 > len(nums)/3:
        return v2
      return None


s = Solution()
print s.majorityElement([1,1,1,1,2,3,4,5,6])
#print s.majorityElement([1,1,1,2,3,4,5,6])
#print s.majorityElement([2,2])
#print s.majorityElement([0,3,4,0])
#print s.majorityElement([0,0,0])
#print s.majorityElement([2,2,1,3])
