from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        edges = set()
        q = [node]
        used = set()
        while q:
            a = q.pop()
            for b in a.neighbors:
                edges.add((a.val, b.val))
                edges.add((b.val, a.val))
                if b not in used:
                    q.append(b)
                    used.add(b)
        res = Node(node.val, None)
        mp = {node.val: res}
        for edge in edges:
            if edge[0] not in mp:
                mp[edge[0]] = Node(edge[0], None)
            if edge[1] not in mp:
                mp[edge[1]] = Node(edge[1], None)
            mp[edge[0]].neighbors.append(mp[edge[1]])
        return res
