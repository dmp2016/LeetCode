class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for sz in range(1, len(s) + 1):
            for ind in range(0, len(s) - sz + 1):
                ind1, ind2 = ind, ind + sz
                s1 = s[ind1:ind2]
                if s1 == s1[::-1]:
                    res += 1
        return res


test = Solution()
print(test.countSubstrings('abc'))
print(test.countSubstrings('aaa'))
print(test.countSubstrings('a' * 1000))
