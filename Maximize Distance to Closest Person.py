from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        ind1 = 0
        while not seats[ind1]:
            ind1 += 1
        a1 = ind1
        ind2 = len(seats) - 1
        while not seats[ind2]:
            ind2 -= 1
        a2 = len(seats) - 1 - ind2

        prev = ind1
        mv = 0
        for ind in range(ind1, ind2 + 1):
            if seats[ind]:
                mv = max(mv, ind - prev)
                prev = ind
        if a1 > max(mv // 2, a2):
            return a1
        if a2 > max(mv // 2, a1):
            return a2
        return mv // 2


test = Solution()
# print(test.maxDistToClosest(seats=[1, 0, 0, 0, 1, 0, 1]))
# print(test.maxDistToClosest(seats=[1, 0, 0, 0]))
# print(test.maxDistToClosest(seats=[0, 1]))
# print(test.maxDistToClosest(seats=[0, 0, 1, 0, 1, 0]))
print(test.maxDistToClosest([0,0,1]))
