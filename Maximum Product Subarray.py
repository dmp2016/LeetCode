from typing import List, Optional
import math


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        ind0 = None
        ind_neg1, ind_neg2 = None, None
        neg_cnt = 1

        def upd_res(ind0: int, ind1: int,
                    ind_neg1: Optional[int], ind_neg2: Optional[int], 
                    neg_cnt: int, res: int):
            if ind0 is None:
                return res
            if neg_cnt > 0 and ind0 < ind1:
                res = max(res, math.prod(nums[ind0: ind1]))
            elif ind_neg1 is not None and ind_neg2 is not None:
                if ind0 < ind_neg2:
                    res = max(res, math.prod(nums[ind0:ind_neg2]))
                if ind_neg1 + 1 < ind1:
                    res = max(res, math.prod(nums[ind_neg1 + 1: ind1]))
            return res

        for ind in range(len(nums)):
            if nums[ind] == 0:
                res = upd_res(ind0, ind, ind_neg1, ind_neg2, neg_cnt, res)
                ind0 = None
                ind_neg1, ind_neg2 = None, None
                neg_cnt = 1
            else:
                if ind0 is None:
                    ind0 = ind
                if nums[ind] < 0:
                    if ind_neg1 is None:
                        ind_neg1 = ind
                    ind_neg2 = ind
                    neg_cnt = -neg_cnt
        if ind0 is not None:
            res = upd_res(ind0, len(nums), ind_neg1, ind_neg2, neg_cnt, res)

        return res


test = Solution()
print(test.maxProduct(nums=[2, 3, -2, 4]))
print(test.maxProduct(nums=[-2, 0, -1]))
print(test.maxProduct(nums=[-2, -3, -1, 0, -2, -2, -2, -2]))
print(test.maxProduct(nums=[2, 3, 0, 4, 3]))
print(test.maxProduct(nums=[6, 3, -10, 0, 2]))
print(test.maxProduct(nums=[0]))
