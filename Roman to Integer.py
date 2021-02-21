class Solution:
    def romanToInt(self, s: str) -> int:
        dg = {'I' : 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for ind in range(len(s) - 1):
            if dg[s[ind]] < dg[s[ind + 1]]:
                res -= dg[s[ind]]
            else:
                res += dg[s[ind]]
        res += dg[s[-1]]
        return res


test = Solution()
print(test.romanToInt(s = "III"))
print(test.romanToInt(s = "IV"))
print(test.romanToInt(s = "IX"))
print(test.romanToInt(s = "LVIII"))
print(test.romanToInt(s = "MCMXCIV"))
