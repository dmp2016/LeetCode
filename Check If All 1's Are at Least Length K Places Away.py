from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        ind1 = 0
        while ind1 < len(nums) and nums[ind1] == 0:
            ind1 += 1
        for ind2 in range(ind1 + 1, len(nums)):
            if nums[ind2] == 1:
                if ind2 - ind1 <= k:
                    return False
                else:
                    ind1 = ind2
        return True        


test = Solution()
print(test.kLengthApart(nums=[1, 0, 0, 0, 1, 0, 0, 1], k=2))
print(test.kLengthApart(nums=[1, 0, 0, 1, 0, 1], k=2))
print(test.kLengthApart(nums=[1, 1, 1, 1, 1], k=0))
print(test.kLengthApart(nums=[0, 1, 0, 1], k=1))
