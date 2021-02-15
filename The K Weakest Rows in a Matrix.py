from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [elem[1] for elem in sorted([(row.count(1), ind) for ind, row in enumerate(mat)])[0:k]]


test = Solution()
print(test.kWeakestRows(mat=
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], k=3))

print(test.kWeakestRows(mat=
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k=2))
