from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ind = m + n - 1
        ind1, ind2 = m - 1, n - 1
        while ind >= 0:
            if ind1 < 0:
                nums1[ind] = nums2[ind2]
                ind2 -= 1
            elif ind2 < 0:
                nums1[ind] = nums1[ind1]
                ind1 -= 1
            else:
                if nums1[ind1] >= nums2[ind2]:
                    nums1[ind] = nums1[ind1]
                    ind1 -= 1
                else:
                    nums1[ind] = nums2[ind2]
                    ind2 -= 1
            ind -= 1


test = Solution()
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
test.merge(nums1, 3, nums2, 3)
print(nums1)

