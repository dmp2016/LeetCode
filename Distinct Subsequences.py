class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cnt0 = [1] * (len(s) + 1)
        cnt1 = [0] * (len(s) + 1)

        for ct in t:
            for ind in range(len(s)):
                if s[ind] == ct:
                    cnt1[ind + 1] = cnt0[ind] + cnt1[ind]
                else:
                    cnt1[ind + 1] = cnt1[ind]
            cnt0 = cnt1
            cnt1 = [0] * (len(s) + 1)
        return cnt0[-1]


test = Solution()
print(test.numDistinct(s="rabbbit", t="rabbit"))
print(test.numDistinct(s="babgbag", t="bag"))
