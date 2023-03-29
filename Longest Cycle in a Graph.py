from typing import List


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        res = -1
        visited = set()
        for v in range(len(edges)):
            if v not in visited:
                part = dict()
                cnt = 0
                while True:
                    part[v] = cnt
                    v = edges[v]
                    cnt += 1
                    if v < 0:
                        break
                    if v in visited:
                        break
                    if v in part:
                        res = max(res, cnt - part[v])
                        break
                visited.update(part)
        return res


test = Solution()
print(test.longestCycle(edges=[3, 3, 4, 2, 3]))
print(test.longestCycle(edges=[2, -1, 3, 1]))
print(test.longestCycle(edges=[3, 4, 0, 2, -1, 2]))
