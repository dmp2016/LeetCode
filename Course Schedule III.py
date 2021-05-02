from typing import List
from heapq import heapify, heappop, heappush
import math


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        cc = []
        res = 0
        cur = 1
        for a in courses:
            if cur + a[0] - 1 <= a[1]:
                res += 1
                cur += a[0]
                heappush(cc, -a[0])
            elif cc:
                b = heappop(cc)
                b = -b
                if a[0] < b and cur - b + a[0] - 1 <= a[1]:
                    cur += a[0] - b
                    heappush(cc, -a[0])
                else:
                    heappush(cc, -b)

        return res


test = Solution()
print(test.scheduleCourse(courses=[[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]))
print(test.scheduleCourse(courses=[[1, 2]]))
print(test.scheduleCourse(courses=[[3, 2], [4, 3]]))
print(test.scheduleCourse(courses=[[1, 2], [2, 3]]))
print(test.scheduleCourse(courses=[[9, 14], [7, 12], [1, 11], [4, 7]]))
print(test.scheduleCourse(courses=[[5, 15], [3, 19], [6, 7], [2, 10], [5, 16], [8, 14], [10, 11], [2, 19]]))
print(test.scheduleCourse(courses=[[7, 17], [3, 12], [10, 20], [9, 10], [5, 20], [10, 19], [4, 18]]))
