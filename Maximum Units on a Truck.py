from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        res = 0
        for item in boxTypes:
            k = min(item[0], truckSize)
            res += k * item[1]
            truckSize -= k
            if not truckSize:
                break
        return res


test = Solution()
print(test.maximumUnits(boxTypes=[[1, 3], [2, 2], [3, 1]], truckSize=4))
print(test.maximumUnits(boxTypes=[[5, 10], [2, 5], [4, 7], [3, 9]], truckSize=10))
