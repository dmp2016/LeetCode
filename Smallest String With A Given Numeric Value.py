class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = ''
        while n > 0:
            n -= 1
            c = k - 26 * n
            c = 1 if c <= 0 else c
            k -= c
            res += chr(c + ord('a') - 1)
        return res


test = Solution()
print(test.getSmallestString(n=3, k=27))
print(test.getSmallestString(n=5, k=73))
test.getSmallestString(n=10**5, k=10*10**5)
