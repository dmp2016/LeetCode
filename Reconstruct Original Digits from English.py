from collections import Counter


class Solution:
    def originalDigits(self, s: str) -> str:

        digits = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 
                  5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
        idents = 'zwxgtrfois'
        ident_val = [0, 2, 6, 8, 3, 4, 5, 1, 9, 7]
        res = []
        cnt = Counter(s)
        for ind, ident in enumerate(idents):
            while cnt[ident] > 0:
                res.append(ident_val[ind])
                for c in digits[ident_val[ind]]:
                    cnt[c] -= 1
        res.sort()
        return ''.join(map(str, res))


test = Solution()
print(test.originalDigits('owoztneoer'))
print(test.originalDigits('fviefuro'))
