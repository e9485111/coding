class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
      if len(nums) < 2:
        return nums
      first = 0
      second = len(nums)-1
      index = 0
      while index <= second:
        if nums[index] == 2:
          nums[index], nums[second] = nums[second], nums[index]
          second -= 1
          continue
        elif nums[index] == 1:
          index += 1
        else:
          nums[index], nums[first] = nums[first], nums[index]
          first += 1
          index += 1
      return None
s=Solution()
nums = [0]
s.sortColors(nums)
print nums
nums = [0,1,2,0,2,1,0,2,2,0,1,2,0,1]
s.sortColors([0,1,2,0,2,1,0,2,2,0,1,2,0,1])
print nums
