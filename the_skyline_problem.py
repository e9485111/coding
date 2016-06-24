import sys
from heapq import *
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        q = []
        serial = 0
        h = []
        ret = []
        for i in buildings:
          q.append((i[0], 'L', i[2], serial))
          q.append((i[1], 'R', 0, serial))
          serial += 1
        q = sorted(q)

        visited = []
        last = -1
        for ind, i in enumerate(q):
          if i[1] == 'R':
            visited.append(i[3])
          else:
            heappush(h, (sys.maxint-i[2], i[2], i[3]))

          if ind == len(q)-1 or q[ind][0] != q[ind+1][0]:
            while(h and h[0][2] in visited):
              heappop(h)
            if not h:
              ret.append([i[0], 0])
            else:
              if not ret:
                ret.append([i[0], h[0][1]])
              else:
                if h[0][1] != ret[-1][1]:
                  ret.append([i[0], h[0][1]])

        return ret




s = Solution()
print s.getSkyline([[1,2,1],[1,2,2],[1,2,3]])
print s.getSkyline([ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ])
