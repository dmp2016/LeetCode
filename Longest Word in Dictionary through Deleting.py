from typing import List
from collections import defaultdict
from bisect import bisect_right


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        c_pos = defaultdict(list)
        for ind, c in enumerate(s):
            c_pos[c].append(ind)
        res = ''
        for elem in d:
            inds = c_pos[elem[0]]
            if inds:
                cur_ind = inds[0]
                for c in elem[1:]:
                    inds = c_pos[c]
                    ind1 = bisect_right(inds, cur_ind)
                    if ind1 < len(inds):
                        cur_ind = inds[ind1]
                    else:
                        break
                else:
                    if len(res) < len(elem) or (len(res) == len(elem) and res > elem):
                        res = elem
        return res        


test = Solution()
print(test.findLongestWord(s="ybabpcplea", d=["aleat", "appleee", "monkey", "plead"]))
print(test.findLongestWord(s="abpcplea", d=["a", "b", "c"]))
