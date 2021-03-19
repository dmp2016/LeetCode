from typing import List
from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque()
        q.append(0)
        visited = set()
        while q:
            cur = q.popleft()
            if cur not in visited:
                visited.add(cur)
                q.extend(rooms[cur])
        return len(visited) == len(rooms)


test = Solution()
print(test.canVisitAllRooms([[1], [2], [3], []]))
print(test.canVisitAllRooms([[1, 3], [3, 0, 1], [2],[0]]))
