from typing import List
import random


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def get_ind(ind: int) -> int:
            ind = ind*2 + 1
            return ind if ind < len(nums) else ind - len(nums) - (1 - len (nums) %2)

        def partition(l: int, r: int):
            i, j = l - 1, r
            v = nums[r]
            while True:
                i += 1
                while nums[get_ind(i)] > v:
                    i += 1
                j -= 1
                while v > nums[get_ind(j)]:
                    if j == l:
                        break
                    j -= 1
                if i >= j:
                    break
                nums[get_ind(i)], nums[get_ind(j)] = nums[get_ind(j)], nums[get_ind(i)]
            nums[get_ind(i)], nums[get_ind(r)] = nums[get_ind(r)], nums[get_ind(i)]
            return i

        def quicksort(l: int, r: int):
            if r <= l:
                return
            i = partition(l, r)
            quicksort(l, i - 1)
            quicksort(i + 1, r)

        quicksort(0, len(nums) - 1)


sz = 8
def get_ind(ind: int) -> int:
    ind = ind*2 + 1
    return ind if ind < sz else ind - sz - (1 - sz %2)

a = 0
for _ in range(0, sz):
    print(a, end = ' ')
    a = get_ind(a)
print()

a = sz - 1
for _ in range(0, sz):
    print(a, end = ' ')
    a = get_ind(a)
print()



test = Solution()
nums = [1, 5, 1, 1, 6, 4]
test.wiggleSort(nums)
print(nums)
nums = [1, 3, 2, 2, 3, 1]
test.wiggleSort(nums)
print(nums)
nums = [1, 5, 1, 1, 6]
test.wiggleSort(nums)
print(nums)
nums = [4,5,5,6]
test.wiggleSort(nums)
print(nums)
