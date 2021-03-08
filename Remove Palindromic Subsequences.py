class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s == '':
            return 0
        elif s == s[::-1]:
            return 1
        else:
            return 2


test = Solution()
print(test.removePalindromeSub('ababa'))
print(test.removePalindromeSub('abb'))
print(test.removePalindromeSub('baabb'))
print(test.removePalindromeSub(''))
