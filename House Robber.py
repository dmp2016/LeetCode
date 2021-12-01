from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        data = [nums[0]]
        if len(nums) > 1:
            data.append(max(data[0], nums[1]))
        for ind in range(2, len(nums)):
            data.append(max(data[ind - 2] + nums[ind], data[ind - 1]))
        return data[-1]


test = Solution()
print(test.rob(nums=[1, 2, 3, 1]))
print(test.rob(nums=[2, 7, 9, 3, 1]))
