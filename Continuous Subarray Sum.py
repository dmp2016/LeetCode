from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        rems = {0}
        prev = nums[0] % k if k != 0 else nums[0]
        sm = prev
        for n in nums[1:]:
            sm += n
            if k != 0:
                sm %= k
                if sm in rems:
                    return True
            else:
                if sm in rems:
                    return True
            rems.add(prev)
            prev = sm
        return False


test = Solution()
print(test.checkSubarraySum([23, 2, 4, 6, 7],  k=6))
print(test.checkSubarraySum([23, 2, 6, 4, 7],  k=6))
print(test.checkSubarraySum([23, 2, 6, 4, 7],  k=0))
print(test.checkSubarraySum([0],  k=0))
print(test.checkSubarraySum([1, 0],  k=2))
print(test.checkSubarraySum([5,0,0],  k=0))
