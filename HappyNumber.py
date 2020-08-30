class Solution:
    def isHappy(self, n: int) -> bool:
        d = {n}
        while n != 1:
            n = sum([int(c)**2 for c in str(n)])
            if n in d:
                return False
            d.add(n)
        return True


test = Solution()
print(test.isHappy(20))
