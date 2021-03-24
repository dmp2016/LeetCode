from typing import List
from heapq import heappop, heapify
from collections import deque


class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        res = [-1] * len(A)
        heapify(A)
        B = [(b, i) for i, b in enumerate(B)]
        heapify(B)
        C = deque()
        while B and A:
            b = heappop(B)
            while A:
                a = heappop(A)
                if a > b[0]:
                    res[b[1]] = a
                    break
                else:
                    C.append(a)
        ind = 0
        while C:
            if res[ind] < 0:
                res[ind] = C.pop()
            ind += 1
        return res


test = Solution()
print(test.advantageCount(A=[2, 7, 11, 15], B=[1, 10, 4, 11]))
print(test.advantageCount(A=[12, 24, 8, 32], B=[13, 25, 32, 11]))
