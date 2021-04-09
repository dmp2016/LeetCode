from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alph = 'abcdefghigklmnopqrstuvwxyz'
        d = dict((b, a) for a, b in enumerate(order))
        for ind in range(1, len(words)):
            if not (''.join([alph[d[c]] for c in words[ind - 1]]) <= ''.join([alph[d[c]] for c in words[ind]])):
                return False
        return True


test = Solution()
print(test.isAlienSorted(words=["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz"))
print(test.isAlienSorted(words=["word", "world", "row"], order="worldabcefghijkmnpqstuvxyz"))
print(test.isAlienSorted(words=["apple","app"], order="abcdefghijklmnopqrstuvwxyz"))
