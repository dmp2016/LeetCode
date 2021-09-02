from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        
        res = 0
        checked = set()
        for k in range(len(nums)):
            if k not in checked:
                ns = set()
                while k not in ns:
                    ns.add(k)
                    k = nums[k]
                checked.update(ns)
                res = max(res, len(ns))
        return res


test = Solution()
print(test.arrayNesting(nums=[5, 4, 0, 3, 1, 6, 2]))
print(test.arrayNesting(nums=[0, 1, 2]))
