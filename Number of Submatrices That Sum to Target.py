from typing import List
from collections import defaultdict


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        res = 0
        for col1 in range(len(matrix[0])):
            rs = [0] * len(matrix)
            for col2 in range(col1, len(matrix[0])):
                for row in range(len(matrix)):
                    rs[row] += matrix[row][col2]
                vs = defaultdict(int)
                vs[0] = 1
                s = 0
                for v in rs:
                    s += v
                    if s - target in vs:
                        res += vs[s - target]
                    vs[s] += 1
        return res


test = Solution()
print(test.numSubmatrixSumTarget(matrix=[[0, 1, 0], [1, 1, 1], [0, 1, 0]], target=0))
print(test.numSubmatrixSumTarget(matrix=[[1, -1], [-1, 1]], target=0))
print(test.numSubmatrixSumTarget(matrix=[[904]], target=0))
