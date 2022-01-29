from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left, right = 0, max(piles)

        while left < right - 1:
            mid = (left + right) // 2
            if sum((a + mid - 1) // mid for a in piles) <= h:
                right = mid
            else:
                left = mid

        return right


test = Solution()
print(test.minEatingSpeed(piles=[3, 6, 7, 11], h=8))
print(test.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=5))
print(test.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=6))
