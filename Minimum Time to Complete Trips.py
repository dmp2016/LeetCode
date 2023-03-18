from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left, right = 0, time[0] * totalTrips
        while left < right - 1:
            mid = (left + right) // 2
            cnt = sum(mid // a for a in time)
            if cnt < totalTrips:
                left = mid
            else:
                right = mid
        return right


test = Solution()
print(test.minimumTime(time=[1, 2, 3], totalTrips=5))
print(test.minimumTime(time=[2], totalTrips=1))
