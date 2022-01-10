class Solution:
    def addBinary(self, a: str, b: str) -> str:
        b = '0' * (len(a) - len(b)) + b
        a = '0' * (len(b) - len(a)) + a
        c = 0
        res = ''
        for ind in range(len(b) - 1, -1, -1):
            m = int(a[ind]) + int(b[ind]) + c
            res += str(m & 1)
            c = m >> 1
        if c:
            res += '1'
        return res[::-1]


test = Solution()
print(test.addBinary(a="11", b="1"))
print(test.addBinary(a="1010", b="1011"))
