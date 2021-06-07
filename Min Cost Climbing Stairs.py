from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost = cost + [0, 0]
        for ind in range(len(cost) - 3, -1, -1):
            cost[ind] = min(cost[ind] + cost[ind + 1], cost[ind] + cost[ind + 2])
        return min(cost[0], cost[1])


test = Solution()
print(test.minCostClimbingStairs(cost=[10, 15]))
print(test.minCostClimbingStairs(cost=[10, 15, 20]))
print(test.minCostClimbingStairs(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
