from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        edges = dict()
        for edge in connections:
            edges.setdefault(edge[0], []).append(edge[1])
            edges.setdefault(edge[1], []).append(edge[0])

        v_set = set(range(n))
        edge_spare = 0
        conn_amount = 0
        while v_set:
            conn_amount += 1
            q = [v_set.pop()]
            vert_subs = set()
            while q:
                v = q.pop()
                vert_subs.add(v)
                for neighbor in edges.get(v, []):
                    if neighbor in v_set:
                        v_set.remove(neighbor)
                        q.append(neighbor)
            edge_amount = 0
            for v in vert_subs:
                edge_amount += len(edges.get(v, []))
            edge_amount //= 2
            edge_spare += edge_amount - (len(vert_subs) - 1)
        if edge_spare >= conn_amount - 1:
            return conn_amount - 1
        else:
            return -1


test = Solution()
print(test.makeConnected(n=4, connections=[[0, 1], [0, 2], [1, 2]]))
print(test.makeConnected(n=6, connections=[[0, 1], [0, 2], [0, 3], [1, 2]]))
