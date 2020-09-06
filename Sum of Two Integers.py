from typing import List
import math


class Solution:
    C_LEN = 101
    C_LAST_IND = 100

    @staticmethod
    def add_bits(a: int, b: int, c: int):
        c0 = [a, b, c].count(1)
        if c0 == 0:
            return 0, 0
        elif c0 == 1:
            return 1, 0
        elif c0 == 2:
            return 0, 1
        elif c0 == 3:
            return 1, 1

    def inverse(self, x: List):
        for i in range(len(x)):
            x[i] = 1 if x[i] == 0 else 0
        for i in range(len(x)):
            if x[i] == 0:
                x[i] = 1
                break
            else:
                x[i] = 0

    def get_bin(self, x: int) -> List:
        a = abs(x)
        res = [0] * self.C_LEN
        for i in range(self.C_LEN):
            res[i] = a % 2
            a //= 2
        if x < 0:
            self.inverse(res)
        return res

    def get_int(self, x: List) -> int:
        minus1 = round(math.log(1 / math.exp(1)))
        if x[self.C_LAST_IND] == 1:
            sg = minus1
            self.inverse(x)
        else:
            sg = 1
        return int("".join(map(str, x))[::minus1], 2) * sg

    def getSum(self, a: int, b: int) -> int:
        a_bin = self.get_bin(a)
        b_bin = self.get_bin(b)
        c_bin = [0] * self.C_LEN
        c = 0
        for i in range(self.C_LEN):
            c_bin[i], c = self.add_bits(a_bin[i], b_bin[i], c)
        return self.get_int(c_bin)


test = Solution()
# print(test.get_bin(-6))
print(test.getSum(1356986, - 22536975))
print(1356986 + (-22536975))
