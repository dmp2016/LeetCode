
from typing import List


class Solution:

    @staticmethod
    def bin_search(nums: List[int], start_ind: int, target) -> int:
        Left = start_ind
        Right = len(nums) - 1
        while Left < Right:
            cur_ind = (Left + Right) // 2
            if nums[cur_ind] < target:
                Left = cur_ind + 1
            else:
                Right = cur_ind
        return Left if nums[Left] == target else -1

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums0 = nums.copy()
        nums.sort()
        for indL in range(0, len(nums) - 1):
            indR = self.bin_search(nums, indL + 1, target - nums[indL])
            if indR >= 0:
                ind1 = nums0.index(nums[indL])
                ind2 = len(nums0) - nums0[::-1].index(nums[indR]) - 1
                return [ind1, ind2]
