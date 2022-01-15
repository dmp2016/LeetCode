from typing import List
from collections import defaultdict


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        vi = defaultdict(list)
        for ind in range(len(arr)):
            vi[arr[ind]].append(ind)
        front = {0}
        used = set()
        res = 0
        while front:
            if len(arr) - 1 in front:
                return res
            used.update(front)
            new_front = set()
            val_used = set()
            for v in front:
                if v > 0 and (v - 1) not in used:
                    new_front.add(v - 1)
                if v < len(arr) - 1 and (v + 1) not in used:
                    new_front.add(v + 1)
                if arr[v] not in val_used:
                    for t in vi[arr[v]]:
                        if t != v and t not in used:
                            new_front.add(t)
                    val_used.add(arr[v])
            front = new_front
            res += 1
        return -1


test = Solution()
# print(test.minJumps(arr = [100,-23,-23,404,100,23,23,23,3,404]))
# print(test.minJumps(arr = [7]))
# print(test.minJumps(arr = [7,6,9,6,9,6,9,7]))
print(test.minJumps(arr = [7] * 100000 + [11]))
