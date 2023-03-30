from collections import Counter
from typing import Tuple
from functools import lru_cache


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        
        @lru_cache(None)
        def do_rec(s1: str, s2: str):
            if len(s1) == 1:
                return s1 == s2
            for i in range(1, len(s1)):
                if do_rec(s1[:i], s2[:i]) and do_rec(s1[i:], s2[i:]):
                    return True
                if do_rec(s1[len(s2) - i:], s2[:i]) and do_rec(s1[:len(s2) - i], s2[i:]):
                    return True
            return False

        return do_rec(s1, s2)


test = Solution()
print(test.isScramble(s1="great", s2="rgeat"))
print(test.isScramble(s1="abcde", s2="caebd"))
print(test.isScramble(s1="a", s2="a"))
print(test.isScramble(s1="abcdbdacbdac", s2="bdacabcdbdac"))
