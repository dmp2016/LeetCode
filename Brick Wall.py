from typing import List
from collections import Counter


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        cnt = Counter()
        for row in range(len(wall)):
            sm = 0
            for col in range(len(wall[row]) - 1):
                sm += wall[row][col]
                cnt[sm] += 1
        mc = cnt.most_common(1)
        return len(wall) - (mc[0][1] if mc else 0)


test = Solution()
# print(test.leastBricks([[1, 2, 2, 1],
#         [3, 1, 2],
#         [1, 3, 2],
#         [2, 4],
#         [3, 1, 2],
#         [1, 3, 1, 1]]))
print(test.leastBricks([[1],[1],[1]]))
