from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        res = []
        ind = 0
        while ind < len(A) and A[ind] < 0:
            ind += 1
        ind1, ind2 = ind - 1, ind
        for ind in range(len(A)):
            if ind1 < 0:
                x = A[ind2] ** 2
                ind2 += 1
            elif ind2 == len(A):
                x = A[ind1] ** 2
                ind1 -= 1
            else:
                if ind1 >= 0 and ind2 <= len(A):
                    if abs(A[ind1]) > abs(A[ind2]):
                        x = A[ind2] ** 2
                        ind2 += 1
                    else:
                        x = A[ind1] ** 2
                        ind1 -= 1
            res.append(x)
        return res


test = Solution()
A = [-4,-1,0,3,10]
print(test.sortedSquares(A))
A = [-7,-3,2,3,11]
print(test.sortedSquares(A))

