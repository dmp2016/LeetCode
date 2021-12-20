from typing import List
import math


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_dif = math.inf
        for ind in range(1, len(arr)):
            if arr[ind] - arr[ind - 1] < min_dif:
                min_dif = arr[ind] - arr[ind - 1]
        return [[arr[ind], arr[ind + 1]] for ind in range(len(arr) - 1) if arr[ind + 1] - arr[ind] == min_dif]


test = Solution()
print(test.minimumAbsDifference(arr = [4,2,1,3]))
print(test.minimumAbsDifference(arr = [1,3,6,10,15]))
print(test.minimumAbsDifference(arr = [3,8,-10,23,19,-4,-14,27]))
