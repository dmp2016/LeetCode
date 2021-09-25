class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1:
            return ''
        for ind in range(len(palindrome)):
            if (len(palindrome) & 1 == 0 or ind != len(palindrome) // 2) and palindrome[ind] > 'a':
                return palindrome[:ind] + 'a' + palindrome[ind + 1:]
        ind = len(palindrome) // 2 - 1
        return palindrome[:-1] + 'b'


test = Solution()
print(test.breakPalindrome('abccba'))
print(test.breakPalindrome('a'))
print(test.breakPalindrome('zz'))
print(test.breakPalindrome('aaa'))
print(test.breakPalindrome('aa'))
print(test.breakPalindrome('aaaaa'))
print(test.breakPalindrome("bbb"))
