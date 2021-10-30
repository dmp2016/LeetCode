class Solution:
    def longestDupSubstring(self, s: str) -> str:

        left, right = 0, len(s)

        while left < right - 1:
            n = (left + right) // 2
            # Check for n-substring
            sbs = set()
            for ind in range(len(s) - n + 1):
                s1 = s[ind:ind + n].__hash__()
                if s1 in sbs:
                    left = n
                    break
                else:
                    sbs.add(s1)
            else:
                right = n

        if left > 0:
            sbs = set()
            for ind in range(len(s) - left + 1):
                s1 = s[ind:ind + left].__hash__()
                if s1 in sbs:
                    return s[ind:ind + left]
                else:
                    sbs.add(s1)

        return ''


test = Solution()
print(test.longestDupSubstring(s="banana"))
print(test.longestDupSubstring(s="abcd"))
