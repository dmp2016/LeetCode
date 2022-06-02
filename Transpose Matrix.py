from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        for j in range(len(matrix[0])):
            res.append([])
            for i in range(len(matrix)):
                res[-1].append(matrix[i][j])
        return res
