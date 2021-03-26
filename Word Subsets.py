from typing import List
from collections import Counter


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        bc = Counter()
        for b in B:
            sbc = Counter(b)
            for c in sbc:
                bc[c] = max(bc[c], sbc[c])
        res = []
        for a in A:
            sac = Counter(a)
            for c in bc:
                if sac[c] < bc[c]:
                    break
            else:
                res.append(a)
        return res


test = Solution()
print(test.wordSubsets(A=["amazon", "apple", "facebook", "google", "leetcode"], B=["e", "o"]))
print(test.wordSubsets(A=["amazon", "apple", "facebook", "google", "leetcode"], B=["l", "e"]))
print(test.wordSubsets(A=["amazon", "apple", "facebook", "google", "leetcode"], B=["e", "oo"]))
print(test.wordSubsets(A=["amazon", "apple", "facebook", "google", "leetcode"], B=["lo", "eo"]))
print(test.wordSubsets(A=["amazon", "apple", "facebook", "google", "leetcode"], B=["ec", "oc", "ceo"]))
