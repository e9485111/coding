class Solution(object):
    def longestIncreasingPath(self, matrix):
        self.mem = {}
        self.matrix = matrix
        ret = 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                tmp = self.helper(i, j)
                ret = max(ret, tmp)
        return ret

    def helper(self, x, y):
        if (x,y) in self.mem:
            return self.mem[(x,y)]
        value = self.matrix[x][y]
        next = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ret = 1
        for i in next:
            if (x + i[0] >= 0 and x + i[0] < len(self.matrix) and
                y + i[1] >= 0 and y + i[1] < len(self.matrix[0]) and
                self.matrix[x + i[0]][y + i[1]] > value
                ):
                ret = max(ret, self.helper(x+i[0], y+i[1]) + 1)
        self.mem[(x,y)] = ret
        return ret


class Solution2(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        self.mem = {}
        ret = ""
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                tmp = self.find(i, j, matrix, [])
                if len(tmp) > len(ret):
                    ret = tmp
        return len(ret)

    def find(self, x, y, matrix, visited):
        v = matrix[x][y]
        if (x,y) in self.mem:
            return [v] + self.mem[(x,y)]
        r=[]
        if (x,y) in visited:
            return []
        visited += [(x,y)]
        if x > 0 and matrix[x-1][y] > v:
            tmp = self.find(x-1, y, matrix, visited)
            if len(tmp) > len(r):
                r = tmp
        if y > 0 and matrix[x][y-1] > v:
            tmp = self.find(x, y-1, matrix, visited)
            if len(tmp) > len(r):
                r = tmp
        if x < len(matrix)-1 and matrix[x+1][y] > v:
            tmp = self.find(x+1, y, matrix, visited)
            if len(tmp) > len(r):
                r = tmp
        if y < len(matrix[0])-1 and matrix[x][y+1] > v:
            tmp = self.find(x, y+1, matrix, visited)
            if len(tmp) > len(r):
                r = tmp
        self.mem[(x,y)] =  r
        return [v] + r

s = Solution()
print s.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]])
print s.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]])



