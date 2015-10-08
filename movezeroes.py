class Solution(object):
  def moveZeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    first = 0
    second = 0
    for i in range(0,len(nums)):
      if nums[i] == 0:
        continue
      else:
        nums[first], nums[i] = nums[i], nums[first]
        first += 1
    for i in range(first, len(nums)):
      nums[i] = 0

s = Solution()
nums = [0,1,0,3,12]
s.moveZeroes(nums)
print nums


