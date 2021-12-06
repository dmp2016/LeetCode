from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        a = sum(elem & 1 for elem in position)
        return min(a, len(position) - a)


test = Solution()
print(test.minCostToMoveChips(position=[1, 2, 3]))
print(test.minCostToMoveChips(position=[2, 2, 2, 3, 3]))
