class Solution:
    def addDigits(self, num: int) -> int:
        if not num:
            return 0
        else:
            return (num - 1) % 9 + 1


test = Solution()
print([test.addDigits(i) for i in range(1000)])
