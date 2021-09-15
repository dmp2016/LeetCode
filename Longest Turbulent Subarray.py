from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        k = 0
        ind2 = 1
        ind1 = 0
        cur_comp = None
        res = 1
        while ind2 < len(arr):
            if arr[ind2 - 1] > arr[ind2]:
                if cur_comp or cur_comp is None:
                    cur_comp = False
                else:
                    res = max(res, ind2 - ind1)
                    cur_comp = False
                    ind1 = ind2 - 1
            elif arr[ind2 - 1] < arr[ind2]:
                if not cur_comp or cur_comp is None:
                    cur_comp = True
                else:
                    res = max(res, ind2 - ind1)
                    cur_comp = False
                    ind1 = ind2 - 1
                cur_comp = True
            else:
                res = max(res, ind2 - ind1)
                cur_comp = True
                ind1 = ind2
                cur_comp = None
            ind2 += 1
        res = max(res, ind2 - ind1)
        return res


test = Solution()
print(test.maxTurbulenceSize(arr=[9, 4, 2, 10, 7, 8, 8, 1, 9]))
print(test.maxTurbulenceSize(arr=[4, 8, 12, 16]))
print(test.maxTurbulenceSize(arr=[100]))
print(test.maxTurbulenceSize(arr=[100, 100]))
