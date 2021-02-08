from typing import List
from heapq import heappush, heappop
from sortedcontainers import SortedList
import math


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        left_part = SortedList([0])
        sum_left = 0
        sum_right = A[0]
        cur_max = sum_right - left_part[0]
        for ind in range(1, len(A)):
            sum_left += A[ind - 1]
            sum_right += A[ind]
            left_part.add(sum_left)
            cur_max = max(cur_max, sum_right - left_part[0])
        d_sum_left = 0
        left_part.remove(d_sum_left)
        sum_left += A[len(A) - 1]
        sum_right += A[0]
        if left_part:
            cur_max = max(cur_max, sum_right - left_part[0])
        for ind in range(1, len(A)):
            d_sum_left += A[ind - 1]
            sum_left += A[ind - 1]
            sum_right += A[ind]
            left_part.remove(d_sum_left)
            left_part.add(sum_left)
            if left_part:
                cur_max = max(cur_max, sum_right - left_part[0])
        return cur_max


test = Solution()
# print(test.maxSubarraySumCircular([1, -2, 3, -2]))
# print(test.maxSubarraySumCircular([5, -3, 5]))
# print(test.maxSubarraySumCircular([3, -1, 2, -1]))
# print(test.maxSubarraySumCircular([3, -2, 2, -3]))
# print(test.maxSubarraySumCircular([-2, -3, -1]))
print(test.maxSubarraySumCircular([-2]))
