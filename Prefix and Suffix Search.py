from typing import List
from collections import defaultdict


class WordFilter:

    def __init__(self, words: List[str]):
        self.pref_ind = defaultdict(set)
        self.suff_ind = defaultdict(set)
        used = set()
        for ind1 in range(len(words) - 1, -1, -1):
            w = words[ind1]
            if w in used:
                continue
            used.add(w)
            for ind2 in range(len(w)):
                self.pref_ind[w[:(ind2 + 1)]].add(ind1)
                self.suff_ind[w[len(w) - 1 - ind2:]].add(ind1)

    def f(self, prefix: str, suffix: str) -> int:
        a = self.pref_ind.get(prefix, set()).intersection(self.suff_ind.get(suffix, set()))
        if a:
            return max(a)
        else:
            return -1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
# test = WordFilter(['apple'])
# print(test.f('a', 'l'))

test = WordFilter(['a'] * 7500 + ['b'] * 7500)
for _ in range(15000):
    test.f('a', 'b')
