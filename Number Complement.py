class Solution:
    def findComplement(self, num: int) -> int:
        a = num
        mask = 1
        while a > 1:
            mask <<= 1
            mask |= 1
            a >>= 1
        return num ^ mask


test = Solution()
print(test.findComplement(5))
print(test.findComplement(1))
