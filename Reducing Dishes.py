from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        res = 0
        d = list(range(1, len(satisfaction) + 1))
        for i in range(len(satisfaction)):
            res = max(sum(a * b for a, b in zip(satisfaction[i:], d[:len(d) - i])), res)
        return res


test = Solution()
print(test.maxSatisfaction(satisfaction=[-1, -8, 0, 5, -9]))
print(test.maxSatisfaction(satisfaction=[4, 3, 2]))
print(test.maxSatisfaction(satisfaction=[-1, -4, -5]))
