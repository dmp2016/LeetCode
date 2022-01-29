from typing import List
import math


class MinTree:
    def get_val(self, ind1: int, ind2: int) -> int:
        res = math.inf
        cur_level = 0
        while ind1 <= ind2:
            if ind1 % 2 == 1:
                res = min(res, self.data[cur_level][ind1])
                ind1 += 1
            if ind1 <= ind2:
                if ind2 % 2 == 0:
                    res = min(res, self.data[cur_level][ind2])
                    ind2 -= 1
            if ind1 <= ind2:
                cur_level += 1
                ind1 //= 2
                ind2 //= 2
        return res

    def build(self):
        step = 2
        for i in range(1, self.level_cnt):
            for j in range(0, self.cust_size // step):
                self.data[i][j] = min([self.data[0][i] for i in range(j * step, j * step + step)])
            step *= 2

    def __init__(self, data: List[int]):
        self.cust_size = 1
        while self.cust_size < len(data):
            self.cust_size *= 2

        self.data = []
        self.data.append(data + [math.inf] * (self.cust_size - len(data)))

        self.level_cnt = 1
        n = self.cust_size // 2
        while n > 0:
            self.data.append([math.inf] * n)
            self.level_cnt += 1
            n //= 2
        self.build()


A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
all_good = True
test_min = MinTree(A)
for i in range(len(A)):
    for j in range(i, len(A) - 1):
        a, b = test_min.get_val(i, j), min(A[i:j + 1])
        print(a, b)
        all_good = all_good and (a == b)

print('Tests min:', 'Ok' if all_good else 'Not ok')
