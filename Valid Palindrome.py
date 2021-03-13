class Solution:
    def isPalindrome(self, s: str) -> bool:
        d = list(map(str.lower, filter(str.isalnum, s)))
        return d == d[::-1]


test = Solution()
print(test.isPalindrome("A man, a plan, a canal: Panama"))
print(test.isPalindrome("0P"))
