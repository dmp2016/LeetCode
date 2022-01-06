from typing import List
from heapq import heappush, heappop, nsmallest


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        q = []
        cur_pas = 0
        for item in trips:
            cur_pas += item[0]
            heappush(q, (item[2], item[0]))
            while q and q[0][0] <= item[1]:
                cur_pas -= heappop(q)[1]
            if cur_pas > capacity:
                return False
        return True


test = Solution()
print(test.carPooling(trips = [[2,1,5],[3,3,7]], capacity = 4))
print(test.carPooling(trips = [[2,1,5],[3,3,7]], capacity = 5))
print(test.carPooling(trips = [[1,1,2],[1,2,3]], capacity = 1))
