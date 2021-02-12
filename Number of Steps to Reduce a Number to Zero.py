class Solution:
    def numberOfSteps (self, num: int) -> int:
        cnt = 0
        while num > 0:
            if num & 1:
                num -= 1
            else:
                num >>= 1
            cnt += 1
        return cnt

test = Solution()
print(test.numberOfSteps(14))
print(test.numberOfSteps(8))