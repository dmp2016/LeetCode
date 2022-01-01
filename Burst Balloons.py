from typing import List, Tuple


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = tuple([1] + nums + [1])
        cache = dict()

        def get_max(nums: Tuple[int]) -> int:
            if len(nums) == 2:
                return 0
            if nums in cache:
                return cache[nums]
            res = 0
            for ind in range(1, len(nums) - 1):
                res = max(res, nums[0] * nums[ind] * nums[-1] + get_max(nums[:ind + 1]) + get_max(nums[ind:]))
            cache[nums] = res
            return res

        return get_max(nums)

test = Solution()
print(test.maxCoins([3, 1, 5, 8]))
print(test.maxCoins([1, 5]))
print(test.maxCoins([8,3,4,3,5,0,5,6,6,2,8,5,6,2,3,8,3,5,1,0,2]))
