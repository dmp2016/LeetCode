from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        d = [(s.count('0'), s.count('1')) for s in strs]
        dp = [[[-1] * (m + 1) for _ in range(n + 1)] for _ in range(len(d))]

        def do_rec(ind0: int, ma: int, na: int) -> int:
            if ind0 == len(d):
                return 0
            if dp[ind0][na][ma] >= 0:
                return dp[ind0][na][ma]
            res = 0
            if ma >= d[ind0][0] and na >= d[ind0][1]:
                res = max(1 + do_rec(ind0 + 1, ma - d[ind0][0], na - d[ind0][1]), do_rec(ind0 + 1, ma, na))
            else:
                res = do_rec(ind0 + 1, ma, na)
            dp[ind0][na][ma] = res
            return res

        return do_rec(0, m, n)


test = Solution()
print(test.findMaxForm(strs=["10", "0001", "111001", "1", "0"], m=4, n=3))
print(test.findMaxForm(strs=["10", "0001", "111001", "1", "0", "1100101", "11", "00"], m=5, n=3))
print(test.findMaxForm(strs=["10", "0001", "111001", "1", "0"], m=5, n=3))
print(test.findMaxForm(strs=["10", "0", "1"], m=1, n=1))
