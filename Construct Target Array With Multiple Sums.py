from typing import List
from heapq import heapify, heappop, heappush, nsmallest
import math


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target[0] == 1
        sm = sum(target)
        target = [-a for a in target]
        heapify(target)
        while True:
            a = -heappop(target)
            b = -heappop(target)
            if a == 1:
                return True
            a1 = 2 * a - sm
            if a1 < 1:
                return False
            if a1 > b:
                c1 = sm
                c2 = a1 - sm
                k = int((b - c1) / c2)
                ak = c1 + k * c2
            else:
                ak = a1
            sm += ak - a
            heappush(target, -b)
            heappush(target, -ak)


test = Solution()
print(test.isPossible(target=[9, 3, 5]))
print(test.isPossible(target=[1, 1, 1, 2]))
print(test.isPossible(target=[8, 5]))
print(test.isPossible(target=[1, 1000000000]))
print(test.isPossible(target=[1, 5, 20, 1000000000]))
print(test.isPossible(target=[2, 900000001]))
