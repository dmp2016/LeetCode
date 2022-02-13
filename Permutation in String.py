from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        tmpl = Counter(s1)
        tmpl
        n = len(s1)
        cur = Counter(s2[:n - 1])
        for i in range(len(s2) - n + 1):
            cur[s2[i + n - 1]] += 1
            if cur == tmpl:
                return True
            cur[s2[i]] -= 1
            if not cur[s2[i]]:
                del cur[s2[i]]
        return False


test = Solution()
print(test.checkInclusion(s1="ab", s2="eidbaooo"))
print(test.checkInclusion(s1="ab", s2="eidboaoo"))
print(test.checkInclusion("adc", "dcda"))
