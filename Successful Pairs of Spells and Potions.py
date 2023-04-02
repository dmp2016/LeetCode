from typing import List
from bisect import bisect_left


class Solution:
    def successfulPairs0(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions.sort()
        for spell in spells:
            left, right = -1, len(potions)
            while left < right - 1:
                mid = (left + right) // 2
                if spell * potions[mid] < success:
                    left = mid
                else:
                    right = mid
            res.append(len(potions) - right)
        return res

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        return [len(potions) - bisect_left(a=potions, x=success / spell) for spell in spells]


t = Solution()
print(t.successfulPairs0(spells=[5, 1, 3], potions=[1, 2, 3, 4, 5], success=7))
print(t.successfulPairs0(spells=[3, 1, 2], potions=[8, 5, 8], success=16))

print(t.successfulPairs(spells=[5, 1, 3], potions=[1, 2, 3, 4, 5], success=7))
print(t.successfulPairs(spells=[3, 1, 2], potions=[8, 5, 8], success=16))
