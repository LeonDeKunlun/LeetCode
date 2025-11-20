class Solution:
    def intersectionSizeTwo(self, intervals: list[list[int]]) -> int:
        interval_dict = dict()
        for start, end in intervals:
            if end not in interval_dict or interval_dict[end] < start:
                interval_dict[end] = start
        intervals = sorted(interval_dict.items())

        left, right = intervals[0][0]-1, intervals[0][0]
        size = 2
        for end, start in intervals:
            if right < start:
                left, right = end-1, end
                size += 2
            elif left < start: # <= right
                if right == end:
                    left = end-1
                else:
                    left, right = right, end
                size += 1
        return size