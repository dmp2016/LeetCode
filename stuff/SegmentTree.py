from typing import List


class SumTree:
    def get_val(self, ind1: int, ind2: int) -> int:
        res = 0
        cur_level = 0
        while ind1 <= ind2:
            if ind1 % 2 == 1:
                res += self.data[cur_level][ind1]
                ind1 += 1
            if ind1 <= ind2:
                if ind2 % 2 == 0:
                    res += self.data[cur_level][ind2]
                    ind2 -= 1
            if ind1 <= ind2:
                cur_level += 1
                ind1 //= 2
                ind2 //= 2
        return res

    def change_delta(self, ind: int, delta: int):
        for i in range(self.level_cnt):
            self.data[i][ind] += delta
            ind //= 2

    def set_element(self, ind: int, new_value: int):
        delta = new_value - self.data[0][ind]
        self.change_delta(ind, delta)

    def build(self):
        step = 2
        for i in range(1, self.level_cnt):
            for j in range(0, self.cust_size // step):
                self.data[i][j] = sum([self.data[0][i] for i in range(j * step, j * step + step)])
            step *= 2

    def __init__(self, data: List[int]):
        self.cust_size = 1
        while self.cust_size < len(data):
            self.cust_size *= 2

        self.data = []
        self.data.append(data + [0] * (self.cust_size - len(data)))

        self.level_cnt = 1
        n = self.cust_size // 2
        while n > 0:
            self.data.append([0] * n)
            self.level_cnt += 1
            n //= 2
        self.build()


A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
all_good = True
test_sum = SumTree(A)
for i in range(len(A)):
    for j in range(i, len(A) - 1):
        a, b = test_sum.get_val(i, j), sum(A[i:j + 1])
        print(a, b)
        all_good = all_good and (a == b)

A[0] = 15
test_sum.set_element(0, 15)
A[4] = 16
test_sum.set_element(4, 16)
A[-1] = 17
test_sum.set_element(len(A) - 1, 17)
for i in range(len(A)):
    for j in range(i, len(A) - 1):
        a, b = test_sum.get_val(i, j), sum(A[i:j + 1])
        print(a, b)
        all_good = all_good and (a == b)

print('Tests sum:', 'Ok' if all_good else 'Not ok')
