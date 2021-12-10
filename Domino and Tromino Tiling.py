class Solution:
    def numTilings(self, n: int) -> int:
        
        cache = dict()
        def do_rec(a: int, b: int) -> int:
            if (a, b) in cache:
                return cache[(a, b)]
            if a > b:
                res = do_rec(b ,a)
            elif a < 0:
                return 0
            elif a == b:
                if a == 0:
                    res = 1
                else:
                    res = (do_rec(a - 1, b - 1) + do_rec(a - 2, b - 2) + do_rec(a - 1, b - 2) + do_rec(a - 2, b - 1)) % 1000000007
            elif a == b - 1:
                res = (do_rec(a, b - 2) + do_rec(a - 1, b - 2)) % 1000000007
            elif a == b - 2:
                res = do_rec(a, b - 2)
            cache[(a, b)] = res
            return res

        return do_rec(n, n)


test = Solution()
print(test.numTilings(n=1))
print(test.numTilings(n=2))
print(test.numTilings(n=3))
print(test.numTilings(n=5))
print(test.numTilings(n=20))
