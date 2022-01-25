from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 1
        while i < len(arr) - 1 and arr[i - 1] < arr[i]:
            i += 1
        if i == 1:
            return False
        while i < len(arr) and arr[i - 1] > arr[i]:
            i += 1
        return i == len(arr)


test = Solution()
print(test.validMountainArray(arr=[2, 1]))
print(test.validMountainArray(arr=[3, 5, 5]))
print(test.validMountainArray(arr=[0, 3, 2, 1]))
print(test.validMountainArray(arr=[5, 3, 2, 1]))
print(test.validMountainArray(arr=[1, 2, 3, 4]))
print(test.validMountainArray(arr=[1]))
