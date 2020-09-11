import numpy as np
from typing import List, Iterator


class Solution:
    @staticmethod
    def getlong1(data):
        ind0, ind1, res = 0, 0, 0
        state = False
        for ind0 in range(len(data)):
            if data[ind0] and not state:
                ind1, state = ind0, True
            if not data[ind0] and state:
                res, state = max([res, ind0 - ind1]), False
        if state:
            res = max([res, ind0 - ind1 + 1])
        return res

    def findLength(self, A: List[int], B: List[int]) -> int:
        A, B = [200] * len(B) + A, B + [300] * len(A)
        res = 0
        for _ in range(1, len(A)):
            A = A[1:]
            B = B[:-1]
            res = max([res, self.getlong1(np.array(A) == np.array(B))])
        return res
