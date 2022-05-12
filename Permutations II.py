from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [nums.copy()]
        last = sorted(nums, key=lambda x: -x)
        while nums != last:
            k = len(nums) - 2
            while k >= 0 and nums[k] >= nums[k + 1]:
                k -= 1
            i = k + 1
            while i < len(nums) - 1 and nums[i + 1] > nums[k]:
                i += 1
            nums[k], nums[i] = nums[i], nums[k]
            i = 1
            while k + i < len(nums) - i:
                nums[k + i], nums[len(nums) - i] = nums[len(nums) - i], nums[k + i]
                i += 1
            res.append(nums.copy())
        return res
        

test = Solution()
print(test.permuteUnique(nums=[1, 1, 2]))
print(test.permuteUnique(nums=[1, 2, 3]))
print(test.permuteUnique(nums=[1, 2, 2, 3, 3, 3]))
