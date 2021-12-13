class Solution:
    def maxPower(self, s: str) -> int:
        cur_char = ''
        cur_p = 0
        res = 0
        for c in s:
            if c != cur_char:
                res = max(res, cur_p)
                cur_p = 1
                cur_char = c
            else:
                cur_p += 1
        return max(res, cur_p)


test = Solution()
print(test.maxPower('leetcode'))
print(test.maxPower('abbcccddddeeeeedcba'))
print(test.maxPower('abbceeccddddeeeeedcba'))
