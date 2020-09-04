class Solution:

    @staticmethod
    def sum2(a: int, b: int, c: int):
        c1 = [a, b, c].count(1)
        if c1 == 0:
            return 0, 0
        elif c1 == 1:
            return 1, 0
        elif c1 == 2:
            return 0, 1
        elif c1 == 3:
            return 1, 1

    def getSum(self, a: int, b: int) -> int:
        if a != 0:
            sg1 = a//abs(a)
        else:
            sg1 = 1
        if b != 0:
            sg2 = b//abs(b)
        else:
            sg2 = 1
        a = abs(a)
        b = abs(b)
        c = 0
        res = []
        while a > 0 or b > 0 or c > 0:
            a1 = a % 2
            b1 = b % 2
            r, c = self.sum2(a1, b1, c)
            res.append(r)
            a //= 2
            b //= 2
        res = res[::-1]
        res = "".join(map(str, res))
        if res == "":
            res = "0"
        return int(res, 2)*sg1*sg2

test = Solution()
print(test.getSum(-1, 8))
