from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]
        horizontalCuts.sort()
        verticalCuts.sort()
        mh_difs = max([horizontalCuts[i + 1] - horizontalCuts[i] for i in range(len(horizontalCuts) - 1)])
        mv_difs = max([verticalCuts[i + 1] - verticalCuts[i] for i in range(len(verticalCuts) - 1)])
        return (mh_difs * mv_difs) % 1000000007


test = Solution()
print(test.maxArea(h=5, w=4, horizontalCuts=[1, 2, 4], verticalCuts=[1, 3]))
print(test.maxArea(h=5, w=4, horizontalCuts=[3, 1], verticalCuts=[1]))
print(test.maxArea(h=5, w=4, horizontalCuts=[3], verticalCuts=[3]))
