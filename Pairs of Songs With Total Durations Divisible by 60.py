from typing import List
from collections import Counter, defaultdict


# Best!!!
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        r = defaultdict(int)
        for a in time:
            r[a % 60] += 1
        res = 0
        for a in time:
            res += r[(-a) % 60]
        res -= r[0] + r[30]
        res >>= 1
        return res


# Slow !
class Solution1:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        r = defaultdict(int)
        for a in time:
            r[a % 60] += 1
        return (sum(r[(-a) % 60] for a in time) - (r[0] + r[30])) >> 1


# Slow!
class Solution2:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        r = Counter(a % 60 for a in time)
        res = sum(r[(-a) % 60] for a in time)
        res -= r[0] + r[30]
        res >>= 1
        return res


test = Solution()
print(test.numPairsDivisibleBy60([30, 20, 150, 100, 40]))
print(test.numPairsDivisibleBy60([60, 60, 60]))
