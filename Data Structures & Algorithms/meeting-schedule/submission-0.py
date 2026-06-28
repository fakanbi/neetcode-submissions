"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sortedINtervals = sorted(intervals, key=lambda x: x.start)
        for i in range(1, len(sortedINtervals)):
            time1 = sortedINtervals[i-1]
            time2 = sortedINtervals[i]

            if time1.end > time2.start:
                return False
            
            
        return True
