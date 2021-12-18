from typing import List

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        sn = str(n)
        res = 0
        for k in range(1, len(sn)):
            res += len(digits) ** k

        def do_rec(snp: str):
            if not snp:
                return 1
            resr = 0
            for c in digits:
                if c < snp[0]:
                    resr += len(digits) ** (len(snp) - 1)
                elif c == snp[0]:
                    resr += do_rec(snp[1:])
                else:
                    break
            return resr

        res += do_rec(sn)
        return res


test = Solution()
print(test.atMostNGivenDigitSet(digits = ["1","3","5","7"], n = 100))
print(test.atMostNGivenDigitSet(digits = ["1","4","9"], n = 1000000000))
print(test.atMostNGivenDigitSet(digits = ["7"], n = 8))
