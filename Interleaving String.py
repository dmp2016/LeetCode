class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if s3:
            if s1 and s1[0] == s3[0]:
                a = self.isInterleave(s1[1:], s2, s3[1:])
            else:
                a = False
            if not a and s2 and s2[0] == s3[0]:
                b = self.isInterleave(s1, s2[1:], s3[1:])
            else:
                b = False
            return a or b
        else:
            return True


test = Solution()
print(test.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))
print(test.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc"))
print(test.isInterleave(s1="", s2="", s3=""))
