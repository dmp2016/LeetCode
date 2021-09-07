from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        ct = 0
        dm = 0
        res = ''
        for ind in range(len(releaseTimes)):
            cd = releaseTimes[ind] - ct
            if cd > dm:
                dm = cd
                res = keysPressed[ind]
            elif cd == dm and res < keysPressed[ind]:
                res = keysPressed[ind]
            ct = releaseTimes[ind]
        return res

test = Solution()
print(test.slowestKey(releaseTimes=[9, 29, 49, 50], keysPressed="cbcd"))
print(test.slowestKey(releaseTimes=[12, 23, 36, 46, 62], keysPressed="spuda"))
