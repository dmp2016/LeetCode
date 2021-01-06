from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for cur in arr:
            if cur > k:
                break
            else:
                k += 1
        return k


test = Solution()
print(test.findKthPositive(arr = [2,3,4,7,11], k = 5))
print(test.findKthPositive(arr = [1,2,3,4], k = 2))
print(test.findKthPositive(arr = [], k = 2))
