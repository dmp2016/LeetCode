from typing import List
from math import gcd


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        dx = x0 - coordinates[1][0]
        dy = y0 - coordinates[1][1]
        g = gcd(dx, dy)
        dx //= g
        dy //= g
        for x, y in coordinates[2:]:
            if dx == 0 and dy == 0:
                if not (x == x0 and y == y0):
                    return False
            elif dx == 0 and dy != 0:
                if not (x == x0 and (y - y0) % dy == 0):
                    return False
            elif dy == 0 and dx != 0:
                 if not (y == y0 and (x - x0) % dx == 0):
                    return False
            else:
                if not ((x - x0) % dx == 0 and (y - y0) % dy == 0 and (x - x0) // dx == (y - y0) // dy):
                    return False
        return True


test = Solution()
print(test.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
print(test.checkStraightLine([[0,0],[0,5],[5,5],[5,0]]))
