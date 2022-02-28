from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if not nums:
            return res
        prev = nums[0]
        left = 0
        for ind in range(1, len(nums)):
            if prev + 1 != nums[ind]:
                if left < ind - 1:
                    res.append(f'{nums[left]}->{nums[ind - 1]}')
                else:
                    res.append(f'{nums[left]}')
                left = ind
            prev = nums[ind]
        if left < len(nums) - 1:
            res.append(f'{nums[left]}->{nums[-1]}')
        else:
            res.append(f'{nums[-1]}')

        return res


test = Solution()
print(test.summaryRanges(nums=[0, 1, 2, 4, 5, 7]))
print(test.summaryRanges(nums=[0, 2, 3, 4, 6, 8, 9]))
