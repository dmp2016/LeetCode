from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        tree = dict()
        for edge in edges:
            tree.setdefault(edge[0], set()).add(edge[1])
            tree.setdefault(edge[1], set()).add(edge[0])

        while len(tree) > 2:
            to_del = set()
            for v in tree:
                if len(tree[v]) == 1:
                    to_del.add(v)
            for v in to_del:
                tree[tree[v].pop()].remove(v)
                del tree[v]
        
        return list(tree.keys())


test = Solution()
print(test.findMinHeightTrees(n = 4, edges = [[1,0],[1,2],[1,3]]))
print(test.findMinHeightTrees(n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]))
print(test.findMinHeightTrees(n = 1, edges = []))
print(test.findMinHeightTrees(n = 2, edges = [[0,1]]))
print(test.findMinHeightTrees(6, [[0,1],[0,2],[0,3],[3,4],[4,5]]))

