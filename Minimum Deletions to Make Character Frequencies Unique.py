from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = sorted(Counter(s).values(), reverse=True)
        res = 0
        a = cnt[0]
        for ind in range(1, len(cnt)):
            b = cnt[ind]
            if b >= a:
                res += min(b - a + 1, b)
                b = a - 1
            a = b
        return res


test = Solution()
# print(test.minDeletions(s="aab"))
# print(test.minDeletions(s="aaabbbcc"))
# print(test.minDeletions(s="ceabaacb"))
print(test.minDeletions(s="abcafacadscavbafsdacsvabvs"))
