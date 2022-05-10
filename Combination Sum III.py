from typing import List, Set


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if sum(range(1, k + 1)) > n or sum(range(9, 9 - k, -1)) < n:
            return []
        
        res = []
        cur_seq = []
        def do_rec(start: int, cur: int, step: int) -> None:
            if step < k:
                for d in range(start, 10):
                    if cur + d > n:
                        break
                    else:
                        cur_seq.append(d)
                        do_rec(d + 1, cur + d, step + 1)
                        cur_seq.pop()
            elif cur == n:
                res.append(cur_seq.copy())
        
        do_rec(1, 0, 0)
        return res


test = Solution()
print(test.combinationSum3(k = 3, n = 7))
print(test.combinationSum3(k = 3, n = 9))
print(test.combinationSum3(k = 4, n = 1))
