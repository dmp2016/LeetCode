class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        nums = [0] * (n + 1)
        nums[1] = 1
        ind = 1
        while ind <= n:
            if 2 * ind <= n:
                nums[2 * ind] = nums[ind]
            if 2 * ind + 1 <= n:
                nums[2 * ind + 1] = nums[ind] + nums[ind + 1]
            ind += 1
        return max(nums)


test = Solution()
# print(test.getMaximumGenerated(n=7))
# print(test.getMaximumGenerated(n=2))
# print(test.getMaximumGenerated(n=3))
# print(test.getMaximumGenerated(n=1))
# print(test.getMaximumGenerated(n=0))
print(test.getMaximumGenerated(n=100))
