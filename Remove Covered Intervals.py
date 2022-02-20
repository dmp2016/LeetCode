from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        b_inds = sorted(list(range(len(intervals))), key=lambda x: -intervals[x][1])
        cnt_rem = 0

        for ind in range(len(intervals) - 1):
            b = intervals[ind][1]
            while b_inds and (b_inds[-1] <= ind or intervals[b_inds[-1]][1] <= b):
                if b_inds[-1] > ind:
                    cnt_rem += 1
                b_inds.pop()
        return len(intervals) - cnt_rem


test = Solution()
print(test.removeCoveredIntervals([[1, 4], [3, 6], [2, 8]]))
print(test.removeCoveredIntervals([[1, 4], [2, 3]]))
print(test.removeCoveredIntervals([[3, 10], [4, 10], [5, 11]]))
print(test.removeCoveredIntervals([[1, 2], [1, 4], [3, 4]]))
