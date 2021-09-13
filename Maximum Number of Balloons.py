from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        t = Counter(text)
        return min([t[key] // val for key, val in Counter('balloon').items()])
        

test = Solution()
print(test.maxNumberOfBalloons(text="nlaebolko"))
print(test.maxNumberOfBalloons(text="loonbalxballpoon"))
print(test.maxNumberOfBalloons(text="leetcode"))
