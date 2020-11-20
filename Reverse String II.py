class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        lst = [s[i:i + k] for i in range(0, len(s), k)]
        return ''.join([lst[i] if i % 2 else lst[i][::-1]  for i in range(len(lst))])


test = Solution()
print(test.reverseStr("abcdefg", 2))
