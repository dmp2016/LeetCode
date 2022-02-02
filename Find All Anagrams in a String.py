from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        s = list(map(ord, s))
        p = list(map(ord, p))
        pt = Counter(p)
        ph = 0
        for c in p:
            ph += c**5
        h0 = 0
        for c in s[:len(p) - 1]:
            h0 += c**5
        res = []
        for ind in range(len(s) - len(p) + 1):
            h0 += s[ind + len(p) - 1]**5
            if h0 == ph:
                if Counter(s[ind:ind + len(p)]) == pt:
                    res.append(ind)
            h0 -= s[ind]**5
        return res


test = Solution()
print(test.findAnagrams(s="cbaebabacd", p="abc"))
print(test.findAnagrams(s="abab", p="ab"))
print(test.findAnagrams(s="aaaaaaaaa", p="a"))
print(test.findAnagrams(s="a", p="a"))
