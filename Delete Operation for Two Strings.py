from functools import lru_cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        @lru_cache(maxsize=None)
        def f(p: int, q: int) -> int:
            if p < 0 or q < 0:
                return 0
            if word1[p] == word2[q]:
                return f(p - 1, q - 1) + 1
            else:
                return max(f(p - 1, q), f(p, q - 1))

        d = f(len(word1) - 1, len(word2) - 1)

        return len(word1) - d + len(word2) - d


test = Solution()
print(test.minDistance(word1="sea", word2="eat"))
print(test.minDistance(word1="leetcode", word2="etco"))
print(test.minDistance(word1="dinitrophenylhydrazine", word2="phenylhydrazine"))
