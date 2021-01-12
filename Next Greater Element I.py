from typing import List
from bisect import bisect_right


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        inds = dict([(b, a) for a, b, in enumerate(nums2)])
        nums2.sort()
        for n in nums1:
            ind = bisect_right(nums2, n)
            res.append(inds[nums2[ind]] if ind < len(nums2) else - 1)
        return res


test = Solution()
print(test.nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 4, 2]))
print(test.nextGreaterElement(nums1=[2, 4], nums2=[1, 2, 3, 4]))
