class Solution:
    def removeStars(self, s: str) -> str:
        ind = len(s) - 1
        skip = 0
        res = ''
        while ind >= 0:
            if s[ind] == '*':
                skip += 1
            elif skip > 0:
                skip -= 1
            else:
                res += s[ind]
            ind -= 1
        return res[::-1]


t = Solution()
print(t.removeStars(s="leet**cod*e"))
print(t.removeStars(s="erase*****"))
