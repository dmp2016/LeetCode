from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp1 = [0] * 1000
        mp2 = [0] * 1000
        for a in nums1:
            mp1[a] += 1
        for a in nums2:
            mp2[a] += 1
        res = []
        for ind in range(1000):
            res += [ind] * min(mp1[ind], mp2[ind])
        return res


test = Solution()
print(test.intersect(nums1=[1, 2, 2, 1], nums2=[2, 2]))
print(test.intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
