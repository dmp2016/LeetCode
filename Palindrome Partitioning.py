from typing import List
from functools import cache


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        @cache
        def do_rec(s: str) -> List[List[str]]:
            res = set()
            if s == s[::-1]:
                res.add((s, ))
            for i in range(1, len(s)):
                left = do_rec(s[:i]) 
                right = do_rec(s[i:])
                for a in left:
                    for b in right:
                        res.add(a + b)
            return res
            
        return list(do_rec(s))


test = Solution()
print(test.partition('aab'))
print(test.partition('a'))
