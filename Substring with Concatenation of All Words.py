from typing import List
from collections import Counter, deque


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        wl = len(words[0])
        for st in range(0, wl):
            used = deque()
            wc = Counter(words)
            for ind in range(st, len(s), wl):
                u = s[ind:ind + wl]
                if wc[u] == 0:
                    while used:
                        elem = used.popleft()
                        wc[elem] += 1
                        if elem == u:
                            break
                if wc[u] > 0:
                    wc[u] -= 1
                    used.append(u)
                    if len(used) == len(words):
                        res.append(ind - wl * (len(words) - 1))
        return res

test = Solution()
print(test.findSubstring(s="barfoothefoobarman", words=["foo", "bar"]))
print(test.findSubstring(s="wordgoodgoodgoodbestword", words=["word", "good", "best", "word"]))
print(test.findSubstring(s="barfoofoobarthefoobarman", words=["bar", "foo", "the"]))
print(test.findSubstring(s="aaa", words=["a", "a"]))
print(test.findSubstring(s="aaaaaaaaaaaaaa", words=["aa", "aa"]))