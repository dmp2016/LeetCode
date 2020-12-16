from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = {}
        stack = []
        for ind, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                res[stack.pop()] = num
            stack.append(ind)
        for num in nums:
            while stack and nums[stack[-1]] < num:
                res[stack.pop()] = num
        return [res.get(ind, -1) for ind in range(len(nums))]


test = Solution()
# print(test.nextGreaterElements([1, 2, 1]))
print(test.nextGreaterElements([100,1,11,1,120,111,123,1,-1,-100]))
