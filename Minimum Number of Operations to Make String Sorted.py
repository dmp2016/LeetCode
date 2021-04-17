class Solution:
    def makeStringSorted(self, s: str) -> int:
        s = list(s)
        res = 0
        while True:
            for i in range(len(s) - 1, 0, -1):
                if s[i] < s[i - 1]:
                    break
            else:
                break
            for j in range(i, len(s)):
                if s[j] >= s[i - 1]:
                    j -= 1
                    break
            s[i - 1], s[j] = s[j], s[i - 1]
            s = s[:i] + (s[i:])[::-1]
            res += 1
        return res


test = Solution()
print(test.makeStringSorted(s="cba"))
print(test.makeStringSorted(s="aabaa"))
print(test.makeStringSorted(s="cdbea"))
print(test.makeStringSorted(s="leetcodeleetcodeleetcode"))
