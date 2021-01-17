import math


class Solution:
    def countVowelStrings(self, n: int) -> int:
        return ((n + 1) * (n + 2) * (n + 3) * (n + 4)) // 24
        return math.prod(list(range(n + 1, n + 5))) // 24


test = Solution()
print(test.countVowelStrings(1))
print(test.countVowelStrings(2))
print(test.countVowelStrings(50))
