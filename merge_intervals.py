# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        overlap = []
        merged = None
        for interval in intervals:
            if not (max(interval.start, new_interval.start) > min(interval.end, new_interval.end)):
                overlap.append(interval)
        if len(overlap) > 0:
            merged = [min(overlap[0].start, new_interval.start), max(overlap[len(overlap)-1].end, new_interval.end)]

        result = []
        for interval in intervals:
            if interval not in overlap:
                result.append(interval)
        if merged:
            result.append(merged)
        # result.sort(key=lambda x : x.start)
        return result
