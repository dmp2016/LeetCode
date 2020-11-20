from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        def check(ind: int):
            return len([0 for s in strs if s[:ind] != strs[0][:ind]]) == 0
        left, right = 0, max(map(len, strs))
        while left < right:
            mid = (left + right) // 2 + 1
            if check(mid):
                left = mid
            else:
                right = mid - 1
        return strs[0][:left]


test = Solution()
strs = ["flower","flow","flight"]
print(test.longestCommonPrefix(strs))
strs = ["dog","racecar","car"]
print(test.longestCommonPrefix(strs))
