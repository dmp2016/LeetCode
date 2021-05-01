from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        dh = [heights[i + 1] - heights[i] for i in range(len(heights) - 1)]

        def check(ind: int) -> bool:
            dt = sorted(dh[:(ind + 1)])
            sb = 0
            for ind in range(len(dt)):
                if dt[ind] > 0:
                    if sb + dt[ind] <= bricks:
                        sb += dt[ind]
                    elif ladders >= len(dt) - ind:
                        return True
                    else:
                        return False
            return True

        if not check(0):
            return 0

        left, right = 0, len(dh) - 1
        while left < right:
            mid = (left + right) // 2 + 1
            if check(mid):
                left = mid
            else:
                right = mid - 1

        return left + 1


test = Solution()
print(test.furthestBuilding(heights=[4, 2, 7, 6, 9, 14, 12], bricks=5, ladders=1))
print(test.furthestBuilding(heights=[4, 12, 2, 7, 3, 18, 20, 3, 19], bricks=10, ladders=2))
print(test.furthestBuilding(heights=[14, 3, 19, 3], bricks=17, ladders=0))
