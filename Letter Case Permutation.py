from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        cnt = len([1 for c in S if c.isalpha()])
        if cnt > 0:
            res = []
            for n in range(1 << cnt):
                k = n
                st = ''
                for c in S:
                    if c.isalpha():
                        if k & 1:
                            st += c.upper() if c.islower() else c.lower()
                        else:
                            st += c
                        k >>= 1
                    else:
                        st += c
                res.append(st)
            return res
        else:
            return [S]


test = Solution()
print(test.letterCasePermutation(S = "a1b2"))
print(test.letterCasePermutation(S = "3z4"))
print(test.letterCasePermutation(S = "12345"))
print(test.letterCasePermutation(S = "0"))
