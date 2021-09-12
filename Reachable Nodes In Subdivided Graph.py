from typing import List
import math
from heapq import heappush, heappop


class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = dict()
        for i in range(n):
            graph[i] = []
        for edge in edges:
            graph[edge[0]].append([edge[1], edge[2]])
            graph[edge[1]].append([edge[0], edge[2]])
        
        # Dijkstra 
        distance = [math.inf] * n
        distance[0] = 0
        pq = []
        heappush(pq, [0, 0])
        processed = set()
        while pq:
            a = heappop(pq)[1]
            if a in processed:
                continue
            processed.add(a)
            for u in graph[a]:
                b = u[0]
                w = u[1] + 1
                if distance[a] + w < distance[b]:
                    distance[b] = distance[a] + w
                    heappush(pq, [distance[b], b])
        
        res = 0
        for d in distance:
            if d <= maxMoves:
                res += 1
        for edge in edges:
            a = maxMoves - distance[edge[0]] if maxMoves - distance[edge[0]] > 0 else 0
            b = maxMoves - distance[edge[1]] if maxMoves - distance[edge[1]] > 0 else 0
            res += min(a + b, edge[2])
        
        return res


test = Solution()
print(test.reachableNodes(edges=[[0, 1, 10], [0, 2, 1], [1, 2, 2]], maxMoves=6, n=3))
print(test.reachableNodes(edges=[[0, 1, 4], [1, 2, 6], [0, 2, 8], [1, 3, 1]], maxMoves=10, n=4))
print(test.reachableNodes(edges=[[1, 2, 4], [1, 4, 5], [1, 3, 1], [2, 3, 4], [3, 4, 5]], maxMoves=17, n=5))
