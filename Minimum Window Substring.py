from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '':
            return ''
        t_set = Counter(t)
        cur_set = Counter()
        ind1 = ind2 = 0
        ind_f1 = ind_f2 = -1
        n = 0
        while ind2 < len(s):
            while ind2 < len(s):
                c = s[ind2]
                ind2 += 1
                cur_set[c] += 1
                if c in t_set.keys() and cur_set[c] == t_set[c]:
                    n += 1
                    if n == len(t_set):
                        break

            if n == len(t_set):
                while n == len(t_set):
                    if ind_f1 < 0 or ind_f2 - ind_f1 > ind2 - ind1:
                        ind_f1, ind_f2 = ind1, ind2
                    if s[ind1] in t_set.keys() and cur_set[s[ind1]] == t_set[s[ind1]]:
                        n -= 1
                    cur_set[s[ind1]] -= 1
                    ind1 += 1

            else:
                break
        return s[ind_f1:ind_f2] if ind_f1 >= 0 else ''


test = Solution()
print(test.minWindow(s="ADOBECODEBANC", t="ABC"))
