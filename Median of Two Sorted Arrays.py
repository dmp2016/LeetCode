from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    @staticmethod
    def search_for_n_left(nums1: List[int], nums2: List[int], n: int) -> int:
        left, right = 0, len(nums1) - 1
        while left <= right:
            mid = (left + right) // 2
            ind1, ind2 = bisect_left(nums2, nums1[mid]), bisect_right(nums2, nums1[mid])
            if n - ind2 <= mid <= n - ind1:
                return nums1[mid]
            elif mid > n - ind1:
                right = mid - 1
            else:
                left = mid + 1
        return None


    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = (len(nums1) + len(nums2) - 1) // 2
        n2 = (len(nums1) + len(nums2)) // 2
        val1 = self.search_for_n_left(nums1, nums2, n1)
        if val1 is None:
            val1 = self.search_for_n_left(nums2, nums1, n1)
        if n1 == n2:
            return val1
        else:
            val2 = self.search_for_n_left(nums1, nums2, n2)
            if val2 is None:
                val2 = self.search_for_n_left(nums2, nums1, n2)
            return (val1 + val2) / 2


test = Solution()
nums1 = [3,4]
nums2 = [1,2,5,6]
print(test.findMedianSortedArrays(nums1, nums2))
nums1 = [1,3]
nums2 = [2]
print(test.findMedianSortedArrays(nums1, nums2))
nums1 = [1,2]
nums2 = [3,4]
print(test.findMedianSortedArrays(nums1, nums2))
nums1 = [0,0]
nums2 = [0,0]
print(test.findMedianSortedArrays(nums1, nums2))
nums1 = []
nums2 = [1]
print(test.findMedianSortedArrays(nums1, nums2))
nums1 = [2]
nums2 = []
print(test.findMedianSortedArrays(nums1, nums2))
