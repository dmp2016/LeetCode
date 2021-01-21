from typing import List
from heapq import heappush, heappop


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        res = []
        pq = []
        m = 0
        for i in range(len(nums) - k + 1):
            heappush(pq, (nums[i], i))
        r = heappop(pq)
        res.append(r[0])
        ind = r[1]
        m += 1
        while m < k:
            new_ind = len(nums) - k + m
            heappush(pq, (nums[new_ind], new_ind))
            r = heappop(pq)
            while r[1] <= ind:
                r = heappop(pq)
            res.append(r[0])
            ind = r[1]
            m += 1
        return res


test = Solution()
print(test.mostCompetitive(nums=[3, 5, 2, 6], k=2))
print(test.mostCompetitive(nums=[2, 4, 3, 3, 5, 4, 9, 6], k=4))
