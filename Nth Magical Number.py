class Solution:

    @staticmethod
    def gcd(a: int, b: int) -> int:
        if a > b:
            a, b = b, a
        
        while True:
            r1 = b % a
            if not r1:
                break
            b, a = a, r1
        return a

    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        if a > b:
            a, b = b, a

        c = self.gcd(a, b)
        a //= c
        b //= c
        q = a * b * c

        m = (a - 1) + (b - 1) + 1
        nm = n % m

        res = (n // m) * q
        if nm > 0:
            tl = [i * a for i in range(1, b)] + [i * b for i in range(1, a)]
            tl.sort()
            res += tl[nm - 1] * c
        return res % 1000000007


# print(Solution.gcd(16, 12))
# print(Solution.gcd(16, 13))
test = Solution()
print(test.nthMagicalNumber(n=1, a=2, b=3))
print(test.nthMagicalNumber(n=4, a=2, b=3))
print(test.nthMagicalNumber(n=5, a=2, b=4))
print(test.nthMagicalNumber(n=3, a=6, b=4))
print(test.nthMagicalNumber(7, 5, 8))
print(test.nthMagicalNumber(1000000001, 3, 99999))
