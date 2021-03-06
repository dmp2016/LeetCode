from typing import List
from bisect import bisect_left


class SumTree:
    def get_val(self, ind1: int, ind2: int):
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

    def change_delta(self, ind, delta):
        for i in range(self.level_cnt):
            self.data[i][ind] += delta
            ind //= 2

    def set_element(self, ind, new_value):
        delta = new_value - self.data[0][ind]
        self.change_delta(ind, delta)

    def build(self):
        step = 2
        for i in range(1, self.level_cnt):
            for j in range(0, self.cust_size // step):
                self.data[i][j] = sum([self.data[0][i] for i in range(j * step, j * step + step)])
            step *= 2

    def __init__(self, data):
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


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        nums_sorted = nums.copy()
        nums_sorted.sort()
        sum_tree = SumTree([1] * len(nums_sorted))
        res = []
        for a in nums:
            ind = bisect_left(nums_sorted, a)
            res.append(sum_tree.get_val(0, ind - 1))
            sum_tree.change_delta(ind, -1)
        return res


test = Solution()
nums = [5, 2, 6, 1]
print(test.countSmaller(nums))
