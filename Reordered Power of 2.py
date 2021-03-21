from collections import Counter
from typing import List


class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:

        def get_digits(n: int) -> List[int]:
            digits = []
            while n > 0:
                digits.append(n % 10)
                n //= 10
            return Counter(digits)

        n_digits = get_digits(N)
        pow2 = 1
        while pow2 <= 1000000000:
            if get_digits(pow2) == n_digits:
                return True
            pow2 <<= 1
        return False


test = Solution()
print(test.reorderedPowerOf2(1))
print(test.reorderedPowerOf2(10))
print(test.reorderedPowerOf2(16))
print(test.reorderedPowerOf2(24))
print(test.reorderedPowerOf2(46))
