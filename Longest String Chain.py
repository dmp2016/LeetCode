from typing import List
from collections import Counter


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: -len(x))

        cl = dict()
        for ind1 in range(len(words)):
            w1 = words[ind1]
            cl[w1] = 1
            for ind2 in range(ind1 - 1, -1, -1):
                w2 = words[ind2]
                if len(w1) + 1 < len(w2):
                    break
                if len(w1) + 1 == len(w2):
                    for ind3 in range(len(w2)):
                        if w2[:ind3] + w2[ind3 + 1:] == w1:
                            cl[w1] = max(cl[w1], cl[w2] + 1)
        return max(cl.values())


test = Solution()
print(test.longestStrChain(words=["a", "b", "ba", "bca", "bda", "bdca"]))
print(test.longestStrChain(words=["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]))
print(test.longestStrChain(words=["qyssedya","pabouk","mjwdrbqwp","vylodpmwp","nfyqeowa","pu","paboukc","qssedya","lopmw","nfyqowa","vlodpmw","mwdrqwp","opmw","qsda","neo","qyssedhyac","pmw","lodpmw","mjwdrqwp","eo","nfqwa","pabuk","nfyqwa","qssdya","qsdya","qyssedhya","pabu","nqwa","pabqoukc","pbu","mw","vlodpmwp","x","xr"]))
