from typing import List
import random


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def sort_custom(cur_list: List[int]) -> List[int]:
            if not cur_list:
                return []

            cur = random.choice(cur_list)
            left = []
            right = []
            mid = []
            for a in cur_list:
                if a < cur:
                    left.append(a)
                elif a == cur:
                    mid.append(a)
                else:
                    right.append(a)
            return sort_custom(left) + mid + sort_custom(right)

        return sort_custom(nums)


test = Solution()
print(test.sortArray(nums=[5, 2, 3, 1]))
print(test.sortArray(nums=[5, 1, 1, 2, 0, 0]))
print(test.sortArray(nums=[0]))
print(test.sortArray(nums=[3, -1]))
print(test.sortArray(nums=[-4, 0, 7, 4, 9, -5, -1, 0, -7, -1]))
