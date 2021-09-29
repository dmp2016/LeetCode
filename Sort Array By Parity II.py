from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ind_even, ind_odd = 0, 1
        for i in range(len(nums)):
            if i & 1 == 0:
                while nums[ind_even] & 1:
                    ind_even += 1
                nums[ind_even], nums[i] = nums[i], nums[ind_even]
            else:
                while nums[ind_odd] & 1 == 0:
                    ind_odd += 1
                nums[ind_odd], nums[i] = nums[i], nums[ind_odd]
            ind_odd = max(ind_odd, i + 1)
            ind_even = max(ind_even, i + 1)
        return nums


test = Solution()
print(test.sortArrayByParityII(nums=[4, 2, 5, 7]))
print(test.sortArrayByParityII(nums=[2, 3]))
print(test.sortArrayByParityII(nums=[1, 1, 2, 2, 2]))
print(test.sortArrayByParityII(nums=[1, 1, 1, 2, 2, 2]))
        