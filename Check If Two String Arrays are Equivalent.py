from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return [c for s in word1 for c in s] == [c for s in word2 for c in s]


test = Solution()
print(test.arrayStringsAreEqual(word1 = ["ab", "c"], word2 = ["a", "bc"]))
