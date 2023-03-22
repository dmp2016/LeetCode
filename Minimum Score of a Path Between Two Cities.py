from typing import List
from math import inf


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        edges = dict()
        for item in roads:
            edges.setdefault(item[0], []).append((item[1], item[2]))
            edges.setdefault(item[1], []).append((item[0], item[2]))
        q = [1]
        visited = set()
        while q:
            v = q.pop()
            visited.add(v)
            for item in edges.get(v, []):
                if item[0] not in visited:
                    q.append(item[0])
        return min(item[1] for v in visited for item in edges.get(v, []))


test = Solution()
print(test.minScore(n=4, roads=[[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]))
print(test.minScore(n=4, roads=[[1, 2, 2], [1, 3, 4], [3, 4, 7]]))
