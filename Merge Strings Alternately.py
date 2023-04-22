class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ''.join(c1 + c2 for c1, c2 in zip(word1, word2))
        return s + word1[len(s) // 2:] + word2[len(s) // 2:]


t = Solution()
print(t.mergeAlternately(word1="abc", word2="pqr"))
print(t.mergeAlternately(word1="ab", word2="pqrs"))
print(t.mergeAlternately(word1="abcd", word2="pq"))
