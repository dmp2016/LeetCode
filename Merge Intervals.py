from typing import List
from heapq import heapify, heappop


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        heapify(intervals)
        res = [heappop(intervals)]
        while intervals:
            r = res[-1][1]
            cur = heappop(intervals)
            if cur[0] <= r:
                res[-1][1] = max(cur[1], res[-1][1])
            else:
                res.append(cur)
        return res


test = Solution()
print(test.merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))
print(test.merge(intervals=[[1, 4], [4, 5]]))
