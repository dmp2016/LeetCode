from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)//2):
            s[i], s[-(i + 1)] = s[-(i + 1)], s[i]


test = Solution()
lst = ["1","2", "3"]
test.reverseString(lst)
print(lst)
        