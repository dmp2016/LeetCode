from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(key=lambda x: -x)
        return nums[k - 1]


test = Solution()
print(test.findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2))
print(test.findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
