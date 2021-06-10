from typing import List
from heapq import heapify, heappush, heappop


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        d = sorted(zip(efficiency, speed))
        ds = sorted([(s, ind) for ind, (_, s) in enumerate(d)], key=lambda x: -x[0])
        mp = dict()
        for i in range(len(ds)):
            mp[ds[i][1]] = i
        res = 0
        fi = set()
        cur_sm = 0
        set_sm = set()
        sm_ind = 0
        for ind in range(len(d)):
            fi.add(mp[ind])
            if mp[ind] in set_sm:
                cur_sm -= ds[mp[ind]][0]
                set_sm.remove(mp[ind])
            sm1 = d[ind][1]
            while len(set_sm) < k - 1 and sm_ind < len(ds):
                if sm_ind not in fi:
                    cur_sm += ds[sm_ind][0]
                    set_sm.add(sm_ind)
                sm_ind += 1
            res = max(res, (sm1 + cur_sm) * d[ind][0])
        return res % 1000000007


test = Solution()
print(test.maxPerformance(n=6, speed=[2, 10, 3, 1, 5, 8], efficiency=[5, 4, 3, 9, 7, 2], k=2))
print(test.maxPerformance(n=6, speed=[2, 10, 3, 1, 5, 8], efficiency=[5, 4, 3, 9, 7, 2], k=3))
print(test.maxPerformance(n=6, speed=[2, 10, 3, 1, 5, 8], efficiency=[5, 4, 3, 9, 7, 2], k=4))
