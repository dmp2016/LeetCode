class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def check(s: str) -> str:
            return s[:len(s) // 2] == s[(len(s) + 1) // 2:][::-1]
        
        L2 = 0
        while not check(s[len(s) - L2:][::-1] + s):
            L2 += 1

        return s[len(s) - L2:][::-1] + s
