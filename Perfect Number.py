class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num % 2 != 0:
            return False
        sum_div = 1
        d = 2
        while d * d < num:
            if num % d == 0:
                sum_div += d + num // d
            d += 1
        if num % (d * d) == 0:
            sum_div += d
        return sum_div == num

test = Solution()
print(test.checkPerfectNumber(28))
print(test.checkPerfectNumber(29))
print(test.checkPerfectNumber(100000000))
