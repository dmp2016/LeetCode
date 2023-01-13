from typing import List


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        edges = dict()
        for ind in range(len(parent)):
            edges.setdefault(parent[ind], []).append(ind)
        self.res = 1

        def dfs(node: int) -> int:
            if not (ve := edges.get(node)):
                return 1

            r = [(dfs(v), v) for v in ve]
            r = sorted([elem[0] for elem in r if s[elem[1]] != s[node]], reverse=True)

            if len(r) >= 2 and r[0] + r[1] + 1 > self.res:
                self.res = r[0] + r[1] + 1
            if len(r) >= 1:
                if r[0] + 1 > self.res:
                    self.res = r[0] + 1
                return r[0] + 1
            else:
                return 1

        dfs(0)
        return self.res

test = Solution()
print(test.longestPath(parent=[-1, 0, 0, 1, 1, 2], s="abacbe"))
print(test.longestPath(parent=[-1, 0, 0, 0], s="aabc"))
print(test.longestPath(parent=[-1], s="z"))
print(test.longestPath(parent=[-1, 0, 1], s="aab"))
