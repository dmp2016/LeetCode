class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ind1, ind2 = 0, 0
        cur_substr_set = set()
        max_len = 0
        while ind2 < len(s):
            if s[ind2] not in cur_substr_set:
                cur_substr_set.add(s[ind2])
                ind2 += 1
                max_len = max(max_len, ind2 - ind1)
            else:
                cur_substr_set.difference_update(s[ind1])
                ind1 += 1
        return max_len

test = Solution()
print(test.lengthOfLongestSubstring("abcabcbb"))
print(test.lengthOfLongestSubstring("bbbbb"))
print(test.lengthOfLongestSubstring("pwwkew"))
print(test.lengthOfLongestSubstring(""))
print(test.lengthOfLongestSubstring("dvdf"))
