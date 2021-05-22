from typing import List
from collections import Counter


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        def get_plist(s: str) -> List[int]:
            r = []
            cd = dict()
            n = 0
            for c in s:
                if not c in cd:
                    cd[c] = n
                    r.append(n)
                    n += 1
                else:
                    r.append(cd[c])
            return r

        pt = get_plist(pattern)
        res = []
        for w in words:
            if pt == get_plist(w):
                res.append(w)
        return res


test = Solution()
print(test.findAndReplacePattern(words=["abc", "deq", "mee", "aqq", "dkd", "ccc"], pattern="abb"))
print(test.findAndReplacePattern(words=["a","b","c"], pattern="a"))
