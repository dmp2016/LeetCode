from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        self.cur = []
        self.res = []

        def do_rec(from_ind: int, cur_target: int):
            if cur_target == 0:
                self.res.append(self.cur.copy())
            elif cur_target > 0:
                for ind in range(from_ind, len(candidates)):
                    a = candidates[ind]
                    self.cur.append(a)
                    do_rec(ind, cur_target - a)
                    self.cur.pop()

        do_rec(0, target)
        return self.res


test = Solution()
print(test.combinationSum(candidates=[2, 3, 6, 7], target=7))
print(test.combinationSum(candidates=[2, 3, 5], target=8))
print(test.combinationSum(candidates=[2], target=1))
