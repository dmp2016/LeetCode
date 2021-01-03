class Solution:
    def countArrangement(self, n: int) -> int:
        sets = [[j - 1 for j in range(1, n + 1) if i % j == 0 or j % i == 0] for i in range(1, n + 1)]
        used = [False] * n
        
        def do_rec(lev: int) -> int:
            if lev == n:
                return 1
            res = 0
            for elem in sets[lev]:
                if not used[elem]:
                    if lev == n - 1:
                        res += 1
                        continue
                    else:
                        used[elem] = True
                        res += do_rec(lev + 1)
                        used[elem] = False
            return res
        return do_rec(0)



test = Solution()
print(test.countArrangement(2))
print(test.countArrangement(3))
print(test.countArrangement(5))
print(test.countArrangement(6))
print(test.countArrangement(7))
print(test.countArrangement(8))
print(test.countArrangement(15))
