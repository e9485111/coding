#!/usr/bin/python
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        v = len(nums) - k
        return self.helper(0, len(nums)-1, nums, v)

    def helper(self, start, end, nums, v):
        if start == end:
          return nums[start]
        pivot = start
        for i in range(start, end):
            if nums[i] < nums[end]:
                nums[pivot], nums[i] = nums[i], nums[pivot]
                pivot += 1
        nums[pivot], nums[end] = nums[end], nums[pivot]
        print start, end, pivot, v, nums[start:end+1]
        if pivot == v:
            return nums[pivot]
        elif pivot > v:
            return self.helper(start, pivot-1, nums, v)
        else:
            return self.helper(pivot+1, end, nums, v)
s = Solution()
print s.findKthLargest([3,1,2,4], 2)
#print s.findKthLargest([1], 1)
#print s.findKthLargest([2,3,1,5,6,4], 6)
