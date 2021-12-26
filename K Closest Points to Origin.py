from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda x: x[0]**2 + x[1]**2)
        return points[:k]


test = Solution()
print(test.kClosest([[1, 3], [-2, 2]], k=1))
print(test.kClosest([[3, 3], [5, -1], [-2, 4]], k=2))
