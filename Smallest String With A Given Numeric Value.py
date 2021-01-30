class Solution:
    # Slow
    def getSmallestString1(self, n: int, k: int) -> str:
        res = ''
        while n > 0:
            n -= 1
            c = k - 26 * n
            c = 1 if c <= 0 else c
            k -= c
            res += chr(c + ord('a') - 1)
        return res

    def getSmallestString(self, n: int, k: int) -> str:
        if (k - n) % 25 == 0:
            c = (k - n) // 25
            a = n - c
            return 'a' * a + 'z' * c
        else:
            c = (k - n) // 25
            b = k - n - 25 * c + 1
            a = k - b - 26 * c
            return 'a' * a + chr(ord('a') + b - 1) + 'z' * c


test = Solution()
print(test.getSmallestString(n=3, k=27))
print(test.getSmallestString(n=5, k=73))
print(test.getSmallestString(n=3, k=26*3))
test.getSmallestString(n=10**5, k=10*10**5)
