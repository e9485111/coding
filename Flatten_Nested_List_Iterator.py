class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nums = []
        self.parse(nestedList)
        self.index = 0
        if self.nums:
          self.hasn = True


    def parse(self, items):
        for i in items:
            if i.isInteger():
                self.nums += [i]
            else:
                self.parse(i)

    def next(self):
        """
        :rtype: int
        """
        ret = self.nums[self.index]
        self.index += 1
        if len(self.nums) == self.index:
            self.hasn = False
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.hasn

s = NestedIterator([[1,1],2,[1,1]])
while s.hasNext():
    print s.next()
