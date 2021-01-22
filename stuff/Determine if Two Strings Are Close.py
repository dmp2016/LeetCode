from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        return sorted(c1.values()) == sorted(c2.values()) and c1.keys() == c2.keys()


test = Solution()
print(test.closeStrings(word1="abc", word2="bca"))
print(test.closeStrings(word1="a", word2="aa"))
print(test.closeStrings(word1="cabbba", word2="abbccc"))
print(test.closeStrings(word1="cabbba", word2="aabbss"))
print(test.closeStrings(word1="uau", word2="ssx"))
