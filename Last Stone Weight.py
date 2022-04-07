from typing import List
from heapq import heapify, heappop, heappush

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapify(stones)
        while len(stones) > 1:
            x = -heappop(stones)
            y = -heappop(stones)
            if x > y:
                heappush(stones, -(x - y))
        return -stones[0] if stones else 0


test = Solution()
print(test.lastStoneWeight(stones=[2, 7, 4, 1, 8, 1]))
print(test.lastStoneWeight(stones=[1]))
print(test.lastStoneWeight(stones=[2, 2]))
