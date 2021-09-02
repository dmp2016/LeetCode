from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def do(left: int, right: int) -> int:
            if left + 1 == right:
                return min(nums[left], nums[right])
            else:
                m = (left + right) // 2
                if nums[left] < nums[m] and nums[m] < nums[right]:
                    return nums[left]
                elif nums[left] < nums[m] and nums[m] > nums[right]:
                    return do(m, right)
                else:
                    return do(left, m)
        return do(0, len(nums) - 1)


test = Solution()
print(test.findMin(nums=[3, 4, 5, 1, 2]))
print(test.findMin(nums=[4, 5, 6, 7, 0, 1, 2]))
print(test.findMin(nums=[11, 13, 15, 17]))
