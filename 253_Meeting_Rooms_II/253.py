# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        from Queue import PriorityQueue
        # O(nlgn)
        Q = PriorityQueue()
        intervals.sort(key=lambda itm: itm.start)
        for i, interval in enumerate(intervals):
            if Q.empty():
                Q.put(interval.end)
            else:
                head = Q.get()
                if head <= interval.start:
                    Q.put(interval.end)
                else:
                    Q.put(interval.end)
                    Q.put(head)
        return Q.qsize()
