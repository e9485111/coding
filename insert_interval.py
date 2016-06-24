# Definition for an interval.
class Interval(object):
  def __init__(self, s=0, e=0):
    self.start = s
    self.end = e

class Solution(object):
  def insert(self, intervals, newInterval):
    """
    :type intervals: List[Interval]
    :type newInterval: Interval
    :rtype: List[Interval]
    """
    ret = []
    for i in intervals:
      if newInterval:
        if newInterval.end < i.start:
          ret.append(newInterval)
          ret.append(i)
          newInterval = None
        elif i.end < newInterval.start:
          ret.append(i)
        else:
          newInterval.start = min(newInterval.start, i.start)
          newInterval.end= max(newInterval.end, i.end)
      else:
        ret.append(i)

    if not ret or newInterval:
      ret.append(newInterval)
    return ret

s = Solution()
r = s.insert([Interval(1,2),
              Interval(3,5),
              Interval(6,7),
              Interval(8,9),
              Interval(12,16)],
              Interval(4,9))
for i in r:
  print i.start, i.end

