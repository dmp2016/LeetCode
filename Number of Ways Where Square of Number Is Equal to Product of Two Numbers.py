from typing import List
from collections import Counter

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        cnt = 0
        A = dict([(nums1[i]**2, i) for i in range(len(nums1))])
        B = dict([(nums2[i]**2, i) for i in range(len(nums2))])
        for j in range(len(nums2)):
            for k in range(j + 1, len(nums2)):
                if nums2[j]*nums2[k] in A:
                    cnt += 2
            if nums2[j]*nums2[j] in A:
                cnt += 1
        for j in range(len(nums1)):
            for k in range(j + 1, len(nums1)):
                if nums1[j]*nums1[k] in B and B[nums1[j]*nums1[k]] != A.get(nums1[j]*nums1[k]):
                    cnt += 2
            if nums1[j]*nums1[j] in B and B[nums1[j]*nums1[j]] != A.get(nums1[j]*nums1[j]):
                cnt += 1
        return cnt


test = Solution()
nums1 = [1,1]
nums2 = [1,1,1]
print(test.numTriplets(nums1, nums2))
