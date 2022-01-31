from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = 0
        for a in accounts:
            m = sum(a)
            if res < m:
                res = m
        return res


test = Solution()
print(test.maximumWealth(accounts=[[1, 2, 3], [3, 2, 1]]))
print(test.maximumWealth(accounts=[[1, 5], [7, 3], [3, 5]]))
print(test.maximumWealth(accounts=[[2, 8, 7], [7, 1, 3], [1, 9, 5]]))
