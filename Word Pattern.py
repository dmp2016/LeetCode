class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        dc = dict()
        dw = dict()
        for c, w in zip(pattern, s.split()):
            if c in dc and dc[c] != w:
                return False
            else:
                dc[c] = w
            if w in dw and dw[w] != c:
                return False
            else:
                dw[w] = c
        return True


test = Solution()
print(test.wordPattern(pattern="abba", s="dog cat cat dog"))
print(test.wordPattern(pattern="abba", s="dog cat cat fish"))
print(test.wordPattern(pattern="aaaa", s="dog cat cat dog"))
print(test.wordPattern(pattern="abba", s="dog dog dog dog"))
