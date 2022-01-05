from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        candidates = [0] * (n + 1)

        for item in trust:
            candidates[item[0]] = -1
            if candidates[item[1]] >= 0:
                candidates[item[1]] += 1

        for ind in range(1, n + 1):
            if candidates[ind] == n - 1:
                return ind
        return -1


test = Solution()
print(test.findJudge(n=2, trust=[[1, 2]]))
print(test.findJudge(n=3, trust=[[1, 3], [2, 3]]))
print(test.findJudge(n=3, trust=[[1, 3], [2, 3], [3, 1]]))
