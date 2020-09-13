from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        max_ind1 = len(arr) - 1
        min_ind2 = 0
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                if max_ind1 == len(arr) - 1:
                    max_ind1 = i + 1
                min_ind2 = i

        res = len(arr)
        for ind1 in range(max_ind1 + 1):
            left, right = 0, len(arr) - 1
            while left < right:
                mid = (left + right) // 2
                is_ok = (ind1 + mid > min_ind2) and ((ind1 == 0) or (ind1 + mid >= len(arr)) or (arr[ind1 - 1] <= arr[ind1 + mid]))
                if is_ok:
                    right = mid
                else:
                    left = mid + 1
            res = min(res, right)
        return res


test = Solution()
arr = [1, 2, 3, 10, 4, 2, 3, 5]
# arr = [5, 4, 3, 2, 1]
# arr = [1, 2, 3]
arr = [1]
arr = list(range(100000, 0, -1))
print(test.findLengthOfShortestSubarray(arr))
