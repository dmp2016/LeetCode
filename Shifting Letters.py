from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        sm = 0
        for a in shifts:
            sm += a
            sm %= 26
        res = ""
        for ind, a in enumerate(shifts):
            res += chr((ord(s[ind]) - ord('a') + sm) % 26 + ord('a'))
            sm -= a
        return res


test = Solution()
print(test.shiftingLetters(s="abc", shifts=[3, 5, 9]))
print(test.shiftingLetters(s="aaa", shifts=[1, 2, 3]))
