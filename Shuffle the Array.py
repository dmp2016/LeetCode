from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = [0] * (2 * n)
        for ind in range(n):
            res[2 * ind] = nums[ind]
            res[2 * ind + 1] = nums[ind + n]
        return res


test = Solution()
print(test.shuffle(nums=[2, 5, 1, 3, 4, 7], n=3))
print(test.shuffle(nums=[1, 2, 3, 4, 4, 3, 2, 1], n=4))
print(test.shuffle(nums=[1, 1, 2, 2], n=2))
