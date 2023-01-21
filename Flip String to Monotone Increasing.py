class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n1 = 0
        for c in s:
            if c != '1':
                n1 += 1
        res = n1
        for ind in range(len(s)):
            if s[ind] == '0':
                n1 -= 1
            else:
                n1 += 1
            if res > n1:
                res = n1
        return res


test = Solution()
print(test.minFlipsMonoIncr(s="00110"))
print(test.minFlipsMonoIncr(s="010110"))
print(test.minFlipsMonoIncr(s="00011000"))
