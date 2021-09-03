from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        d = [(a, ind) for ind, a in enumerate(nums)]
        d.sort()
        for ind in range(1, len(d)):
            if d[ind][0] - d[ind - 1][0] <= t and abs(d[ind][1] - d[ind - 1][1]) <= k:
                return True
        return False


test = Solution()
# print(test.containsNearbyAlmostDuplicate(nums=[1, 2, 3, 1], k=3, t=0))
# print(test.containsNearbyAlmostDuplicate(nums=[1, 0, 1, 1], k=1, t=2))
# print(test.containsNearbyAlmostDuplicate(nums=[1, 5, 9, 1, 5, 9], k=2, t=3))
print(test.containsNearbyAlmostDuplicate(nums=[1, 3, 6, 2], k=1, t=2))
