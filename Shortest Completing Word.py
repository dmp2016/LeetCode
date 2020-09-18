from typing import List
from collections import Counter


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        words.sort(key=lambda x: len(x))
        orig_dict = Counter([a.lower() for a in licensePlate if a.isalpha()])
        for s in words:
            sc = Counter(s)
            for c in orig_dict:
                if orig_dict[c] > sc.get(c, 0):
                    break
            else:
                return s


test = Solution()
licensePlate = "1s3 PSt"
words = ["step", "steps", "stripe", "stepple"]
print(test.shortestCompletingWord(licensePlate, words))
licensePlate = "1s3 456"
words = ["looks", "pest", "stew", "show"]
print(test.shortestCompletingWord(licensePlate, words))
