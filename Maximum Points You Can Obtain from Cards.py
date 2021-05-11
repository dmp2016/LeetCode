from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if k < n:
            sc = sum(cardPoints[:n - k])
            mn = sc
            for i in range(k):
                sc = sc - cardPoints[i] + cardPoints[n - k + i]
                if mn > sc:
                    mn = sc
            return sum(cardPoints) - mn
        else:
            return sum(cardPoints)


test = Solution()
print(test.maxScore(cardPoints=[1, 2, 3, 4, 5, 6, 1], k=3))
print(test.maxScore(cardPoints=[2, 2, 2], k=2))
print(test.maxScore(cardPoints=[9, 7, 7, 9, 7, 7, 9], k=7))
