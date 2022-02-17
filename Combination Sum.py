from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        dt = {0: set()}
        for _ in range(500):
            for a in candidates:
                r = list(dt.keys())
                for b in r:
                    if a + b <= target:
                        st = False
                        dt.setdefault(a + b, set()).add((b, a))

        cur = [[target]]
        res = []
        while True:
            st = True
            for t in cur:
                if t[0] > 0:
                    for b, a in dt.get(t[0], []):
                        res.append([b, a] + t[1:])
                        st = False
                else:
                    res.append(t)
            if st:
                res = set(tuple(sorted(d[1:])) for d in res)
                return res
            else:
                cur = res
                res = []


test = Solution()
print(test.combinationSum(candidates=[2, 3, 6, 7], target=7))
print(test.combinationSum(candidates=[2, 3, 5], target=8))
print(test.combinationSum(candidates=[2], target=1))
