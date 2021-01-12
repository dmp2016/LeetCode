class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = s[::(numRows - 1) * 2]
        for i in range(1, numRows - 1):
            cnt = 0
            ind = i
            while ind < len(s):
                res += s[ind]
                ind += (numRows - i - 1) * 2 if cnt % 2 == 0 else i * 2
                cnt += 1
        res += s[numRows - 1::(numRows - 1) * 2]
        return res


test = Solution()
print(test.convert('PAYPALISHIRING', 3))
print(test.convert('PAYPALISHIRING', 4))
print(test.convert('A', 10))
print(test.convert('', 10))
