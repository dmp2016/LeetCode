from functools import lru_cache


class Solution:
    def numberOfArrays0(self, s: str, k: int) -> int:
        n = len(s)

        @lru_cache
        def do_rec(start: int) -> int:
            if start >= n:
                return 0
            if s[start] == '0':
                return 0
            i = start + 1
            res = 0
            while (d := int(s[start:i]) <= k) and i <= n:
                res += do_rec(i)
                i += 1
            if i > n and d <= k:
                res += 1
            return res % 1000000007
        
        return do_rec(0)

    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        dyn = [0] * n
        start = n - 1
        while start >= 0:
            if s[start] == '0':
                dyn[start] = 0
            else:
                i = start
                dyn[start] = 0
                while int(s[start:i + 1]) <= k and i < n - 1:
                    dyn[start] += dyn[i + 1]
                    i += 1
                if i == n - 1 and int(s[start:]) <= k <= k:
                    dyn[start] += 1
                dyn[start] %= 1000000007
            start -= 1
        return dyn[0]


t = Solution()
print(t.numberOfArrays(s="1000", k=10000))
print(t.numberOfArrays(s="1000", k=10))
print(t.numberOfArrays(s="1317", k=2000))
