from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        am = 1 << 30
        mask = 0
        res = 0
        for _ in range(31):
            mask |= am
            part = {a & mask for a in nums}
            tmp_res = res | am
            if any(tmp_res ^ a in part for a in part):
                res = tmp_res
            am >>= 1
        return res


test = Solution()
print(test.findMaximumXOR(nums=[3, 10, 5, 25, 2, 8]))
print(test.findMaximumXOR(nums=[14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]))
