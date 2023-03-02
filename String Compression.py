from typing import List
from itertools import groupby


class Solution:
    def compress(self, chars: List[str]) -> int:
        res = []
        for key, d in groupby(chars):
            res.append(key)
            if (v := len(list(d))) > 1:
                res += list(str(v))
        chars.clear()
        chars.extend(res)
        return len(chars)


test = Solution()
print(test.compress(chars=["a", "a", "b", "b", "c", "c", "c"]))
print(test.compress(chars=["a"]))
print(test.compress(chars=["a", "b", "b", "b", "b",
      "b", "b", "b", "b", "b", "b", "b", "b"]))
