from typing import List
from collections import Counter

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cd = Counter(words)
        a = True
        res = 0
        for item, cnt in cd.most_common():
            if item[0] == item[1]:
                if a and cnt & 1:
                    res += cnt * 2
                    a = False
                else:
                    res += 4 * (cnt // 2)
            else:
                if item[1] + item[0] in cd:
                    res += 2 * min(cnt, cd[item[1] + item[0]])
        return res


test = Solution()
print(test.longestPalindrome(words = ["lc","cl","gg"]))
print(test.longestPalindrome(words = ["ab","ty","yt","lc","cl","ab"]))
print(test.longestPalindrome(words = ["cc","ll","xx"]))
print(test.longestPalindrome(words = ["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]))
