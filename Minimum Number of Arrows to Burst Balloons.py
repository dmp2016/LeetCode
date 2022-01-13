from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        ind = 0
        res = 0
        while ind < len(points):
            bound = points[ind][1]
            ind += 1
            while ind < len(points) and points[ind][0] <= bound:
                bound = min(points[ind][1], bound)
                ind += 1
            res += 1
        return res


test = Solution()
print(test.findMinArrowShots(points = [[10,16],[2,8],[1,6],[7,12]]))
print(test.findMinArrowShots(points = [[1,2],[3,4],[5,6],[7,8]]))
print(test.findMinArrowShots(points = [[1,2],[2,3],[3,4],[4,5]]))
print(test.findMinArrowShots([[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]))
