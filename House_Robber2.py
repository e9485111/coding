class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
          return 0
        parent = {'R':[], 'N':[]}
        DP = {"R":[0]*len(nums), "N":[0]*len(nums)}
        DP['R'][0] = nums[0]
        DP['N'][0] = 0
        for i in range(1, len(nums)):
          DP['R'][i] = DP['N'][i-1]+nums[i]
          parent['R'] += ['N']

          first = DP['R'][i-1]
          second = DP['N'][i-1]
          if first >second:
            parent['N'] += ['R']
          else:
            parent['N'] += ['N']
          DP['N'][i] = max(DP['R'][i-1], DP['N'][i-1])

        if DP['R'][-1] > DP['N'][-1]:
          last = 'R'
        else:
          last = 'N'
        head = last
        i = len(parent['R']) - 1
        while i>=0:
          head = parent[head][i]
          i -= 1

        if last == 'R' and head == 'R':
            DP = {"R":[0]*len(nums), "N":[0]*len(nums)}
            DP['R'][0] = -1
            DP['N'][0] = 0
            for i in range(1, len(nums)):
              DP['R'][i] = DP['N'][i-1]+nums[i]
              DP['N'][i] = max(DP['R'][i-1], DP['N'][i-1])

            return max(DP['R'][-1], DP['N'][-1])
        else:
            return max(DP['R'][-1], DP['N'][-1])




s = Solution()
print s.rob([3,2,1,3])
