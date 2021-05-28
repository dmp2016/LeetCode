from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        res = 0
        sets = [set(w) for w in words]
        for i in range(len(sets)):
            for j in range(i + 1, len(sets)):
                if len(sets[i].intersection(sets[j])) == 0:
                    res = max(res, len(words[i] * words[j]))
        return res
