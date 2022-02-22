class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        p = 1
        for c in columnTitle[::-1]:
            res += (ord(c) - ord("A") + 1) * p
            p *= 26
        return res


test = Solution()
print(test.titleToNumber(columnTitle="Z"))
print(test.titleToNumber(columnTitle="AA"))
print(test.titleToNumber(columnTitle="AB"))
print(test.titleToNumber(columnTitle="ZY"))