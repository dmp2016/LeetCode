from typing import List
import math


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        left_ind = math.inf
        right_ind = s.find(c)
        result = []
        for ind in range(len(s)):
            if ind == right_ind:
                left_ind, right_ind = right_ind, s.find(c, ind + 1)
                if right_ind == -1:
                    right_ind = math.inf
            result.append(min(abs(ind - left_ind), abs(ind - right_ind)))
        return result


test = Solution()
print(test.shortestToChar(s="loveleetcode", c="e"))
print(test.shortestToChar(s="aaab", c="b"))
