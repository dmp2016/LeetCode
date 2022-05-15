from concurrent.futures import process
from typing import List
import math
from heapq import heappush, heappop


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = dict()
        for u, v, w in times:
            g.setdefault(u, []).append((v, w))
        distance = [math.inf] * n
        distance[k - 1] = 0
        q = [(0, k)]
        processed = set()
        while q:
            u = heappop(q)
            if u[1] in processed:
                continue
            processed.add(u[1])
            for v in g.get(u[1], []):
                if distance[u[1] - 1] + v[1] < distance[v[0] - 1]:
                    distance[v[0] - 1] = distance[u[1] - 1] + v[1]
                    heappush(q, (distance[v[0] - 1], v[0]))
        res = max(distance)
        return res if res < math.inf else -1


test = Solution()
print(test.networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2))
print(test.networkDelayTime(times=[[1, 2, 1]], n=2, k=1))
print(test.networkDelayTime(times=[[1, 2, 1]], n=2, k=2))
print(test.networkDelayTime([[1, 2, 1], [2, 3, 7], [1, 3, 4], [2, 1, 2]], 4, 1))
