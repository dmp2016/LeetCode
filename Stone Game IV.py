
from functools import cache



class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        d = [None] * (n + 1)
        def do_rec(n: int) -> bool:
            if not n:
                return False
            if d[n] is not None:
                return d[n]
            k = i = 1
            while k <= n:
                if not do_rec(n - k):
                    d[n] = True
                    return True
                i += 1
                k = i * i
            d[n] = False
            return False
            
        return do_rec(n)


# Slow
class Solution1:
    def winnerSquareGame(self, n: int) -> bool:

        d = [False] * (n + 1)

        for i in range(n + 1):
            k = 1
            while i + k * k <= n:
                d[i + k * k] = d[i + k * k] or not d[i]
                k += 1
        return d[n]


test = Solution()
print(test.winnerSquareGame(n=1))
print(test.winnerSquareGame(n=2))
print(test.winnerSquareGame(n=4))
