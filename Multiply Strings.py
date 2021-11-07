class Solution:
    @staticmethod
    def add_str(num1: str, num2: str) -> str:
        res = []
        dc = 0
        ind = 1
        while ind <= max(len(num1), len(num2)) or dc:
            c1 = int(num1[-ind]) if ind <= len(num1) else 0
            c2 = int(num2[-ind]) if ind <= len(num2) else 0
            c = c1 + c2 + dc
            dc = c // 10
            res.append(str(c % 10))
            ind += 1
        res.reverse()
        return ''.join(res)

    @staticmethod
    def mul_d(num: str, d: str) -> str:
        res = []
        d = int(d)
        dc = 0
        ind = 1
        while ind <= len(num) or dc:
            c = int(num[-ind]) * d if ind <= len(num) else 0
            c += dc
            res.append(str(c % 10))
            dc = c // 10
            ind += 1
        res.reverse()
        return ''.join(res)

    def multiply(self, num1: str, num2: str) -> str:
        res = '0'
        shift = 0
        for c in num2[::-1]:
            a = self.mul_d(num1, c) + '0' * shift
            res = self.add_str(res, a)
            shift += 1
        res[:-1].lstrip('0') + res[-1]
        return res[:-1].lstrip('0') + res[-1]


test = Solution()
print(test.multiply('123', '456'))
print(test.multiply('123', '0'))
print(test.multiply('0', '0'))
