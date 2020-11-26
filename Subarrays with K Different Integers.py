class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        ind1, ind2 = 0, 0
        cur_set = set()
        cnt = 0
        while ind2 < len(A):
            if len(cur_set) < K:
                ind2 += 1
                cur_set.add(A[ind2])
            elif
            if A[ind2] not in cur_set:
                cur_set.add(Aind2])
                ind2 += 1
                max_len = max(max_len, ind2 - ind1)
            else:
                cur_substr_set.difference_update(s[ind1])
                ind1 += 1
        return max_len


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