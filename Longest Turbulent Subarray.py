from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        sa = [arr[ind - 1] - arr[ind] for ind in range(1, len(arr))]
        res = 1
        ind = 0
        while ind < len(sa):
            if sa[ind] != 0:
                i = ind + 1
                while i < len(sa) and (sa[i] > 0 and sa[i - 1] < 0 or sa[i] < 0 and sa[i - 1] > 0):
                    i += 1
                res = max(res, i - ind + 1)
                ind = i
            else:
                ind += 1
        return res


test = Solution()
print(test.maxTurbulenceSize(arr=[9, 4, 2, 10, 7, 8, 8, 1, 9]))
print(test.maxTurbulenceSize(arr=[4, 8, 12, 16]))
print(test.maxTurbulenceSize(arr=[100]))
print(test.maxTurbulenceSize(arr=[100, 100]))
