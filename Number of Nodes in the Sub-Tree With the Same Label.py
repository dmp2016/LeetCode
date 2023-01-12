from typing import List, Optional


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

        labels = list(labels)
        res = [0] * n

        vv = dict()
        for elem in edges:
            vv.setdefault(elem[0], list()).append(elem[1])
            vv.setdefault(elem[1], list()).append(elem[0])

        def dfs(root: int, prev: Optional[int]) -> dict:
            r = dict()
            for a in vv.get(root, []):
                if a != prev:
                    for c, d in dfs(a, root).items():
                        r[c] = r.get(c, 0) + d
            r[labels[root]] = r.get(labels[root], 0) + 1
            res[root] = r[labels[root]]

            return r

        dfs(0, None)

        return res


test = Solution()
print(test.countSubTrees(n=7, edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], labels="abaedcd"))
print(test.countSubTrees(n=4, edges=[[0, 1], [1, 2], [0, 3]], labels="bbbb"))
print(test.countSubTrees(4, [[0, 2], [0, 3], [1, 2]], "aeed"))
