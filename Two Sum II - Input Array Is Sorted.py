from typing import List
from bisect import bisect_left


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for ind in range(len(numbers) - 1):
            t = target - numbers[ind]
            ind2 = bisect_left(numbers, t, lo=ind + 1)
            if ind + 1 <= ind2 < len(numbers) and t == numbers[ind2]:
                return [ind + 1, ind2 + 1]


test = Solution()
print(test.twoSum(numbers=[2, 7, 11, 15], target=9))
print(test.twoSum(numbers=[2, 3, 4], target=6))
print(test.twoSum(numbers=[-1, 0], target=-1))
