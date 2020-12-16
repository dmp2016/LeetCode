from typing import List
from queue import LifoQueue

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = dict()
        stack = LifoQueue()
        for num in nums2:
            stack.
            while stack and stack[-1] < num:
                res[stack.pop()] = num
            stack.append(num)
        return [res.get(m, -1) for m in nums1]


test = Solution()
print(test.nextGreaterElement([4,1,2], [1,3,4,2]))
print(test.nextGreaterElement(nums1=[2, 4], nums2=[1, 2, 3, 4]))
