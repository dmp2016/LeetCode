from collections import defaultdict
from typing import List


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        sums = defaultdict(int)
        sums[0] = 1
        sm = 0
        res = 0
        for n in A:
            sm += n
            sm %= K
            sums[sm] += 1
            res += sums[sm] - 1
        return res


test = Solution()
print(test.subarraysDivByK(A = [4,5,0,-2,-3,1], K = 5))
