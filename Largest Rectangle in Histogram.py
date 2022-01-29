from typing import List, Tuple
import math


class MinTree:
    def get_val(self, ind1: int, ind2: int) -> Tuple[int, int]:
        res = (math.inf, 0)
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
        self.data.append(data + [(math.inf, 0)] * (self.cust_size - len(data)))

        self.level_cnt = 1
        n = self.cust_size // 2
        while n > 0:
            self.data.append([(math.inf, 0)] * n)
            self.level_cnt += 1
            n //= 2
        self.build()


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [(n, ind) for ind, n in enumerate(heights)]
        min_tree = MinTree(heights)
        self.res = 0

        def check_for_int(left: int, right: int) -> None:
            if left > right:
                return
            elem = min_tree.get_val(left, right)
            self.res = max(self.res, elem[0] * (right - left + 1))
            check_for_int(left, elem[1] - 1)
            check_for_int(elem[1] + 1, right)
        
        check_for_int(0, len(heights) - 1)
        return self.res


test = Solution()
print(test.largestRectangleArea(heights = [2, 1, 5, 6, 2, 3]))
print(test.largestRectangleArea(heights = [2, 4]))
