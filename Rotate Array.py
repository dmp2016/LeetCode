from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def shift(k: int, n: int) -> None:
            if k % n == 0:
                return
            elif k > n // 2:
                shift(n // 2, n)
                shift(k - n // 2, n)
            else:
                start_pos = n - k
                for _ in range(n // k - 1):
                    for d in range(k):
                        p1 = start_pos + d
                        p2 = start_pos + d - k
                        nums[p1], nums[p2] = nums[p2], nums[p1]
                    start_pos -= k
                shift(k, n % k + k)

        n = len(nums)
        k %= n
        shift(k, n)
        

test = Solution()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(test.rotate(nums, k=3))
print(nums)
nums = [-1, -100, 3, 99]
print(test.rotate(nums, k=2))
print(nums)
nums = [1,2]
test.rotate(nums, k=1)
print(nums)