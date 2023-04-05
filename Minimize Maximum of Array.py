from typing import List


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = nums[0]
        store = 0
        for i in range(1, len(nums)):
            if res >= nums[i]:
                store += res - nums[i]
            elif nums[i] - res <= store:
                store -= nums[i] - res
            else:
                a = nums[i] - store - res
                res += a // (i + 1)
                if a % (i + 1) > 0:
                    res += 1
                    store = (i + 1) - a % (i + 1)
                else:
                    store = 0
        return res


t = Solution()
# print(t.minimizeArrayValue(nums=[3, 7, 1, 6]))
# print(t.minimizeArrayValue(nums=[10, 1]))
print(t.minimizeArrayValue(nums=[2, 7, 9, 19, 5, 19]))
