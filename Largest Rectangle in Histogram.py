from typing import List, Tuple
import math


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        heights = [0] + heights + [0]
        st = []
        for ind in range(len(heights)):
            while st and heights[st[-1]] > heights[ind]:
                left = st.pop()
                res = max(res, heights[left] * (ind - st[-1] - 1))
            st.append(ind)
        return res


test = Solution()
print(test.largestRectangleArea(heights = [2, 1, 5, 6, 2, 3]))
print(test.largestRectangleArea(heights = [2, 4]))
print(test.largestRectangleArea(heights = [2, 1, 2]))
