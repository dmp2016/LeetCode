from typing import List
from collections import defaultdict


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = set(['a', 'e', 'i', 'o', 'u'])

        set_words = set(wordlist)
        d_lower = defaultdict(str)
        d_vowel = defaultdict(str)

        for w in wordlist:
            if w.lower() not in d_lower:
                d_lower[w.lower()] = w

        for w in wordlist:
            wt = ''.join(map(lambda x: '*' if x.lower() in vowels else x.lower(), w))
            if wt not in d_vowel:
                d_vowel[wt] = w

        res = []
        for w in queries:
            if w in set_words:
                res.append(w)
                continue
            if w.lower() in d_lower:
                res.append(d_lower[w.lower()])
                continue
            wt = ''.join(map(lambda x: '*' if x.lower() in vowels else x.lower(), w))
            if wt in d_vowel:
                res.append(d_vowel[wt])
                continue
            res.append('')
        return res


test = Solution()
print(test.spellchecker(wordlist=["KiTe", "kite", "hare", "Hare"], queries=["kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti", "keet", "keto"]))
print(test.spellchecker(wordlist=["YellOw"], queries=["yollow"]))
