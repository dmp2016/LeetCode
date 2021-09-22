from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        arr = [s for s in arr if len(s) == len(set(s))]
        if not arr:
            return 0
        arr_len = [len(s) for s in arr]
        arr_forbidden = []
        arr_allowed = []
        for ind1 in range(len(arr)):
            arr_forbidden.append(set())
            arr_allowed.append([])
            a = set(arr[ind1])
            for ind2 in range(ind1 + 1, len(arr)):
                if a.intersection(arr[ind2]):
                    arr_forbidden[-1].add(ind2)
                else:
                    arr_allowed[-1].append(ind2)

        def max_from_ind(ind: int, cur_forbidden: set) -> int:
            res = 0
            forb_next = cur_forbidden.union(arr_forbidden[ind])
            for ind_next in arr_allowed[ind]:
                if ind_next not in cur_forbidden:
                    res = max(res, max_from_ind(ind_next, forb_next))
            return res + arr_len[ind]

        return max([max_from_ind(ind, set()) for ind in range(len(arr))])


test = Solution()
print(test.maxLength(arr=["un", "iq", "ue"]))
print(test.maxLength(arr=["cha", "r", "act", "ers"]))
print(test.maxLength(arr=["abcdefghijklmnopqrstuvwxyz"]))
print(test.maxLength(arr=["aa"]))
print(test.maxLength(arr=["a", "abc", "d", "de", "def"]))