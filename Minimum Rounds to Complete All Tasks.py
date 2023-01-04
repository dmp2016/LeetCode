from typing import List
from collections import Counter


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        res = 0
        cnt = Counter(tasks)
        for a in cnt.values():
            if a < 2:
                return -1
            res += a // 3
            if a % 3:
                res += 1
        return res


test = Solution()
# print(test.minimumRounds(tasks=[2, 2, 3, 3, 2, 4, 4, 4, 4, 4]))
# print(test.minimumRounds(tasks=[2, 3, 3]))
print(test.minimumRounds(tasks=[5, 5, 5, 5]))
print(test.minimumRounds(tasks=[5, 5, 5, 5, 5]))
print(test.minimumRounds(tasks=[5, 5, 5, 5, 5, 5]))
