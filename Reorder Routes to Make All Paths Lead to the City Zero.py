from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = dict()
        rev = dict()
        for item in connections:
            edges.setdefault(item[0], []).append(item[1])
            rev.setdefault(item[1], []).append(item[0])

        res = 0
        q = [0]
        visited = set()
        while q:
            v = q.pop()
            visited.add(v)
            for v_next in rev.get(v, []):
                if v_next not in visited:
                    q.append(v_next)
            for v_next in edges.get(v, []):
                if v_next not in visited:
                    res += 1
                    q.append(v_next)
            
        return res


test = Solution()
print(test.minReorder(n=6, connections=[
      [0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]))
print(test.minReorder(n=5, connections=[[1, 0], [1, 2], [3, 2], [3, 4]]))
print(test.minReorder(n=3, connections=[[1, 0], [2, 0]]))
