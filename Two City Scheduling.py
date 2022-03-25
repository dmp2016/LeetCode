from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        n = len(costs) // 2
        return sum(costs[ind][0] + costs[ind + n][1] for ind in range(n))


test = Solution()
print(test.twoCitySchedCost(costs=[[10, 20], [30, 200], [400, 50], [30, 20]]))
print(test.twoCitySchedCost(costs=[[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]))
print(test.twoCitySchedCost(costs=[[515, 563], [451, 713],[537, 709], [343, 819], [855, 779], [457, 60], [650, 359], [631, 42]]))
