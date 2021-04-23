class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        cnt = [0, 0]
        prev = None
        for c in s:
            ind = int(c == '1')
            cnt[ind] = 1 if prev != c else cnt[ind] + 1
            if cnt[1 - ind] >= cnt[ind]:
                res += 1
            prev = c
        return res


test = Solution()
print(test.countBinarySubstrings("00110011"))
print(test.countBinarySubstrings("10101"))
