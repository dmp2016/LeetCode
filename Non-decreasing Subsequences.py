from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        item_list0 = [[i] for i in range(len(nums))]
        res = set()

        is_continue = True
        while is_continue:
            is_continue = False
            item_list1 = []
            for item in item_list0:
                for ind in range(item[-1] + 1, len(nums)):
                    if nums[ind] >= nums[item[-1]]:
                        item_list1.append(item + [ind])
                        is_continue = True
            res.update([tuple(nums[ind] for ind in ind_list) for ind_list in item_list1])
            item_list0 = item_list1

        return list(res)


test = Solution()
print(test.findSubsequences(nums=[4, 6, 7, 7]))
print(test.findSubsequences(nums=[4, 4, 3, 2, 1]))
