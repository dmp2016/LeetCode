from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = 2 ** (len(s) - 1)
        res = []
        for k in range(n):
            k |= n
            t = ''
            item = []
            for i in range(len(s)):
                t += s[i]
                if k & 1:
                    if t != t[::-1]:
                        break
                    else:
                        item.append(t)
                        t = ''
                k >>= 1
            else:
                res.append(item)
        return res



test = Solution()
print(test.partition('aab'))
print(test.partition('a'))
