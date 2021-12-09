from typing import List
from collections import deque


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque()
        q.append(start)
        visited = set()
        while q:
            v = q.popleft()
            if v not in visited:
                visited.add(v)
                for next in [v - arr[v], v + arr[v]]:
                    if 0 <= next < len(arr):                    
                        if arr[next] == 0:
                            return True
                        else:
                            q.append(next)
                    
        return False


test = Solution()
print(test.canReach(arr=[4, 2, 3, 0, 3, 1, 2], start=5))
print(test.canReach(arr=[4, 2, 3, 0, 3, 1, 2], start=0))
print(test.canReach(arr=[3, 0, 2, 1, 2], start=2))
