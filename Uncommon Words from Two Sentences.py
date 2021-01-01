from typing import List
from collections import Counter


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        A1 = Counter(A.split())
        B1 = Counter(B.split())
        return [w for w in A1.keys() if A1[w] == 1 and not w in B1] + [w for w in B1.keys() if B1[w] == 1 and not w in A1]


test = Solution()
print(test.uncommonFromSentences(A = "this apple is sweet", B = "this apple is sour"))
print(test.uncommonFromSentences(A = "apple apple", B = "banana"))

