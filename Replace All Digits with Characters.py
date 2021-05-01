class Solution:
    def replaceDigits(self, s: str) -> str:
        s1 = []
        for ind in range(len(s) // 2):
            c1 = s[2 * ind]
            d2 = ord(s[2 * ind + 1]) - ord('0')
            s1.append(c1)
            s1.append(chr(ord(c1) + d2))
        if len(s) & 1:
            s1.append(s[-1])
        return ''.join(s1)


test = Solution()
print(test.replaceDigits('a1c1e1'))
print(test.replaceDigits('a1b2c3d4e'))
