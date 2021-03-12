class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        A = set([s[ind:ind + k] for ind in range(len(s) - k + 1)])
        return len(A) == (1 << k)


test = Solution()
print(test.hasAllCodes(s="00110", k=2))
print(test.hasAllCodes(s="0110", k=1))
print(test.hasAllCodes(s="0110", k=2))
print(test.hasAllCodes(s="0000000001011100", k=4))
