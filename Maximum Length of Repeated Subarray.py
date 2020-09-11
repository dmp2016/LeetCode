from typing import List, Iterator

# Fastest
# class Solution:
#     def findLength(self, A: List[int], B: List[int]) -> int:
#         szA, szB = len(A), len(B)
#         A, B = [200] * len(B) + A, B + [300] * len(A)
#         res = 0
#         for i in range(1, len(A)):
#             ind1, state = 0, False
#             for j in range(max(szB - i, 0), min(len(A) - i, len(A) - szA + 1)):
#                 if A[i + j] == B[j] and not state:
#                     ind1, state = j, True
#                 if A[i + j] != B[j] and state:
#                     res, state = max([res, j - ind1]), False
#             if state:
#                 res = max([res, len(A) - i - ind1])
#         return res


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        szA, szB = len(A), len(B)
        res = 0
        for i in range(1, szA + szB):
            ind1, state = 0, False
            for j in range(max(szB - i, 0), min(szA + szB - i, szB)):
                if A[i + j - szB] == B[j] and not state:
                    ind1, state = j, True
                if A[i + j - szB] != B[j] and state:
                    res, state = max([res, j - ind1]), False
            if state:
                res = max([res, min(szA + szB - i, szB) - ind1])
        return res


A = [1, 2, 3, 2, 1]
B = [3, 2, 1, 4, 7]
A = [0] * 1000
B = [0] * 1000
# A = [0,0,0,0,1]
# B = [1,0,0,0,0]

test = Solution()
print(test.findLength(A, B))
