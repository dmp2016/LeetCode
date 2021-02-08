from typing import List
from heapq import heappush, heappop
import math


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        sum_all = sum(A)
        sum_left = 0
        min_left = math.inf
        max_left = -math.inf
        sum_right = A[0]
        cur_max = sum_all
        for ind in range(0, len(A) - 1):
            min_left = min(min_left, sum_left)
            max_left = max(max_left, sum_left)
            cur_max = max(cur_max, sum_right - min_left)
            cur_max = max(cur_max, sum_all - (sum_right - max_left))
            sum_left += A[ind]
            sum_right += A[ind + 1]
        return cur_max


test = Solution()
print(test.maxSubarraySumCircular([1, -2, 3, -2]))
print(test.maxSubarraySumCircular([5, -3, 5]))
print(test.maxSubarraySumCircular([3, -1, 2, -1]))
print(test.maxSubarraySumCircular([3, -2, 2, -3]))
print(test.maxSubarraySumCircular([-2, -3, -1]))
print(test.maxSubarraySumCircular([-2]))
