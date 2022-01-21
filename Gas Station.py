from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        start = 0
        while start < len(gas):
            ind = start
            cur = cnt = 0
            while cnt < len(gas):
                cur += gas[ind] - cost[ind]
                if cur < 0:
                    break
                cnt += 1
                ind = (ind + 1) % len(gas)
            else:
                return start
            start += cnt + 1
        return -1


test = Solution()
print(test.canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))
print(test.canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]))
print(test.canCompleteCircuit([6,0,1,3,2], [4,5,2,5,5]))
