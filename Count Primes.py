class Solution:
    def countPrimes1(self, n: int) -> int:
        if n <= 1:
            return 0
        if n == 2:
            return 1
        res = 1
        a = 2
        for i in range(3, n + 1):
            while a * a < i:
                a += 1
            for d in range(2, a + 1):
                if i % d == 0:
                    break
            else:
                res += 1
        return res

    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        g = [1] * n
        g[0] = g[1] = 0
        for i in range(2, n):
            if g[i] == 1:
                j = 2 * i
                while j < n:
                    g[j] = 0
                    j += i
        return sum(g)


test = Solution()
print(test.countPrimes(2))
print(test.countPrimes(100000))
