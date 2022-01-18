from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        flowerbed = [0] + flowerbed + [0]
        for ind in range(1, len(flowerbed) - 1):
            if flowerbed[ind - 1] == 0 and flowerbed[ind + 1] == 0 and flowerbed[ind] == 0:
                n -= 1
                if n == 0:
                    return True
                flowerbed[ind] = 1
        return False


test = Solution()
print(test.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=1))
print(test.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=2))
