from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        res = 0
        words.sort(key=lambda x: -len(x))
        wordset = set(words)
        for word in words:
            if word not in wordset:
                continue
            wordset.remove(word)
            for ind in range(len(word)):
                if word[ind:] in wordset:
                    wordset.remove(word[ind:])
            res += 1 + len(word)
        return res


test = Solution()
# print(test.minimumLengthEncoding(words=["time", "me", "bell"]))
# print(test.minimumLengthEncoding(words=["t"]))
print(test.minimumLengthEncoding(words=["ctxdic","c"]))
