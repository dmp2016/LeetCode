from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freqs = Counter(s)
        for ind in range(len(s)):
            if freqs[s[ind]] == 1:
                return ind
        return -1
        

test = Solution()
print(test.firstUniqChar('leetcode'))
print(test.firstUniqChar('loveleetcode'))
