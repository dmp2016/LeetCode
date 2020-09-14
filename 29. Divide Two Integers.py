class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sgn = -1
        else:
            sgn = 1
        dividend, divisor = abs(dividend), abs(divisor)
        a = bin(dividend)[2:]
        res = ''
        ind = len(bin(divisor)[2:])
        a0 = int(a[:ind], 2)
        if a0 < divisor:
            ind += 1
            a0 = int(a[:ind], 2)
        if a0 < divisor:
                return 0
        res = res + '1'
        temp = bin(a0 - divisor)[2:]
        while ind < len(a):
            temp = temp + a[ind]
            if int(temp, 2) >= divisor:
                res = res + '1'
                temp = bin(int(temp, 2) - divisor)
            else:
                res = res + '0'
            ind += 1
        res = int(res, 2) * sgn
        return res if -2**31 <= res <= 2**31 - 1 else 2**31 - 1


test = Solution()
print(test.divide(42, 5))
print(test.divide(42, -5))
print(test.divide(-2147483648, -1), 2147483648/1)
