from typing import List, Set
from itertools import combinations
from collections import Counter


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k or len(nums) < k:
            return False
        target = sum(nums) // k

        def do_rec(part_num: int, available: List[int]) -> bool:
            if part_num == k:
                return True
            for m in range(1, len(available) - (k  - part_num - 2)):
                for comb in combinations(available, m):
                    if sum(comb) == target:
                        new_available = []
                        c_comb = Counter(comb)
                        for a in available:
                            if c_comb[a] > 0:
                                c_comb[a] -= 1
                            else:
                                new_available.append(a)
                        if do_rec(part_num + 1, new_available):
                            return True
            return False
        
        return do_rec(0, nums)


test = Solution()
print(test.canPartitionKSubsets(nums=[4, 3, 2, 3, 5, 2, 1], k = 4))
print(test.canPartitionKSubsets(nums=[1, 2, 3, 4], k=3))
print(test.canPartitionKSubsets(nums=range(16), k=9))
