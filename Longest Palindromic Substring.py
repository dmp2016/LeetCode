class Solution:
    @staticmethod
    def check(n: int, s: str) -> str:
        for i in range(len(s) - n + 1):
            if s[i:i + n] == s[i:i + n][::-1]:
                return s[i:i + n]
        return ''

    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        left, right = 0, len(s) // 2
        while left < right:
            mid = (left + right) // 2 + 1
            if self.check(2 * mid, s):
                left = mid
            else:
                right = mid - 1
        res1 = self.check(2 * left, s)
        left, right = 0, (len(s) - 1) // 2
        while left < right:
            mid = (left + right) // 2 + 1
            if self.check(2 * mid + 1, s):
                left = mid
            else:
                right = mid - 1
        res2 = self.check(2 * left + 1, s)
        return res1 if len(res1) > len(res2) else res2


test = Solution()
# print(test.check(3, 'babad'))
# print(test.check(2, 'cbbd'))
#print(test.check(2, 'abcba'))

print(test.longestPalindrome('abcba'))
print(test.longestPalindrome('cbbd'))
print(test.longestPalindrome('ac'))
print(test.longestPalindrome('a'))
print(test.longestPalindrome('aa'))
print(test.longestPalindrome(''))
