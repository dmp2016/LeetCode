class Solution:
    def bitwiseComplement(self, n: int) -> int:
        mask = 1
        n1 = n >> 1
        while n1:
            mask = (mask << 1) | 1
            n1 >>= 1
        return n ^ mask


test = Solution()
print(test.bitwiseComplement(5))
print(test.bitwiseComplement(10))
