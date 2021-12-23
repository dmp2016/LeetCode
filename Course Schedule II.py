from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = dict()
        for a, b in prerequisites:
            graph.setdefault(b, []).append(a)

        visited = set()
        ts = []
        self.imp = False
        cur_path = set()

        def dfs(u: int):
            if self.imp:
                return
            visited.add(u)
            cur_path.add(u)
            if u in graph:
                for v in graph[u]:
                    if v in cur_path:
                        self.imp = True
                    if self.imp:
                        break
                    if v not in visited:
                        dfs(v)

            cur_path.remove(u)
            ts.append(u)

        for i in range(numCourses):
            if i not in visited:
                dfs(i)
            if self.imp:
                return []

        ts.reverse()
        return ts


test = Solution()
print(test.findOrder(numCourses=2, prerequisites=[[1, 0]]))
print(test.findOrder(numCourses=4, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]]))
print(test.findOrder(numCourses=1, prerequisites=[]))
print(test.findOrder(2, [[0, 1], [1, 0]]))
