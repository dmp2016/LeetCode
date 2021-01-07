from sortedcontainers import SortedList


class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        combs = {}
        for a in range(k ** (n - 1)):
            s = ''
            for _ in range(n - 1):
                s += str(a % k)
                a //= k
            combs[s] = list(map(str, range(k)))
        res = '0' * (n - 1)
        for _ in range((k ** n)):
            c = combs[res[len(res) - (n - 1):]].pop()
            res += c
        return res


test = Solution()
print(test.crackSafe(n=1, k=2))
print(test.crackSafe(n=2, k=2))
print(test.crackSafe(n=2, k=3))
