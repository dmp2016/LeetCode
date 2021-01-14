from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ind1, ind2 = 0, len(people) - 1
        res = 0
        while ind1 <= ind2:
            if people[ind1] + people[ind2] <= limit:
                ind1 += 1
                ind2 -= 1
            else:
                ind2 -= 1
            res += 1
        return res


test = Solution()
print(test.numRescueBoats(people=[1, 2], limit=3))
print(test.numRescueBoats(people=[3, 2, 2, 1], limit=3))
print(test.numRescueBoats(people=[3, 5, 3, 4], limit=5))
print(test.numRescueBoats(people=[2, 4], limit=5))