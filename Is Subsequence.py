class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        while s and t:
            if s[-1] == t[-1]:
                s.pop()
            t.pop()
        return not s


test = Solution()
print(test.isSubsequence(s="abc", t="ahbgdc"))
print(test.isSubsequence(s="axc", t="ahbgdc"))
