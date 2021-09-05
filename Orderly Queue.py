from collections import Counter

class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            ms = s
            for _ in range(len(s)):
                s = s[-1] + s[:-1]
                if s < ms:
                    ms = s
            return ms
        else:
            s1 = ''.join(sorted(s))[:k]
            s2 = ''
            cs = Counter(s1)
            for c in s:
                if cs[c] == 0:
                    s2 += c
                else:
                    cs[c] -= 1
            return s1 + ''.join(sorted(s2))


test = Solution()
print(test.orderlyQueue(s="cba", k=1))
print(test.orderlyQueue(s="baaca", k=3))
print(test.orderlyQueue("hsdjshyqtehdhsghgduygghq", 5))
print(test.orderlyQueue(s="p", k=1))
