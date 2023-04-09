from typing import List, Tuple, Set


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:

        dict_edges = dict()
        for v1, v2 in edges:
            dict_edges.setdefault(v1, []).append(v2)

        self.cache = dict()
        self.visited = set()

        def do_rec(v: int) -> dict:
            cached = self.cache.get(v)
            if cached:
                return cached
            self.visited.add(v)
            res = dict()
            for neighbour in dict_edges.get(v, []):
                if neighbour in self.visited:
                    raise Exception()
                neib_max_cols = do_rec(neighbour)
                for key in neib_max_cols:
                    res[key] = max(res.get(key, 0), neib_max_cols[key] )
            res[colors[v]] = res.get(colors[v], 0) + 1
            self.cache[v] = res
            self.visited.remove(v)
            return res

        try:
            res = 0
            for i in range(len(colors)):
                cur = do_rec(i).values()
                if cur:
                    res = max(res, max(cur))
            return res
        except:
            return -1


t = Solution()
# print(t.largestPathValue(colors="abaca",
#       edges=[[0, 1], [0, 2], [2, 3], [3, 4]]))
# print(t.largestPathValue(colors="a", edges=[[0, 0]]))
print(t.largestPathValue(colors="hhqhuqhqff", edges=[[0, 1], [0, 2], [2, 3], [3, 4], 
                                                     [3, 5], [5, 6], [2, 7], [6, 7], [7, 8], [3, 8], [5, 8], [8, 9], [3, 9], [6, 9]]))
