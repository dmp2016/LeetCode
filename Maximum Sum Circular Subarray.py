from typing import List
import math


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        left, right = 0, 0
        cur_sum = 0
        max_sum = -math.inf
        A = 2 * A
        while right < len(A):
            cur_sum += A[right]
            max_sum = max(cur_sum, max_sum)
            while cur_sum <= 0 and left < right:
                cur_sum -= A[left]
                left += 1
            max_sum = max(cur_sum, max_sum)
            right += 1
        return max_sum


test = Solution()
print(test.maxSubarraySumCircular([1, -2, 3, -2]))
print(test.maxSubarraySumCircular([5, -3, 5]))
print(test.maxSubarraySumCircular([3, -1, 2, -1]))
print(test.maxSubarraySumCircular([-2, -3, -1]))
