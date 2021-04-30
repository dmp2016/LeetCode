from typing import List


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        res = set()
        xi = 1
        while xi < bound:
            yi = 1
            while True:
                d = xi + yi
                if d <= bound:
                    res.add(d)
                else:
                    break
                if y == 1:
                    break
                else:
                    yi *= y
            if x == 1:
                break
            else:
                xi *= x
        return list(res)


test = Solution()
print(test.powerfulIntegers(x=1, y=3, bound=10))
print(test.powerfulIntegers(x=2, y=1, bound=10))
print(test.powerfulIntegers(x=1, y=1, bound=10))
print(test.powerfulIntegers(x=2, y=3, bound=10))
print(test.powerfulIntegers(x=3, y=5, bound=15))
