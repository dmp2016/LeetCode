class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        for ind in range(n // 2):
            if s[ind] != s[n - ind - 1]:
                d1 = s[ind + 1:n - ind]
                d2 = s[ind:n - ind - 1]
                return d1 == d1[::-1] or d2 == d2[::-1]
        return True


test = Solution()
print(test.validPalindrome("aba"))
print(test.validPalindrome("abca"))
print(test.validPalindrome("abc"))
