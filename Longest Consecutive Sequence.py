from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = set(nums)
        res = 0
        while len(d) > 0:
            a = d.pop()
            tmp_res = 1
            b = a + 1
            while b in d:
                tmp_res += 1
                d.remove(b)
                b += 1
            b = a - 1
            while b in d:
                tmp_res += 1
                d.remove(b)
                b -= 1
            res = max(res, tmp_res)
        return res


test = Solution()
print(test.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))
print(test.longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
