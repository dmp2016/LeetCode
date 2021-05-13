from typing import List


class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:

        def check_num(snum: str) -> bool:
            return not ((snum.find('.') < 0 or snum.find('.') > 1) and len(snum) > 1 and snum[0] == '0') \
                and not (snum.find('.') >= 0 and snum[-1] == '0') \
                and not (len(snum) > 1 and snum[:2] == '00')

        def get_nums(snum: str) -> List[str]:
            res = []
            if check_num(snum):
                res.append(snum)
            for i in range(1, len(snum)):
                a = snum[:i] + '.' + snum[i:]
                if check_num(a):
                    res.append(a)
            return res

        res = []
        for i in range(2, len(s) - 1):
            a_list = get_nums(s[1:i])
            b_list = get_nums(s[i:-1])
            for a in a_list:
                for b in b_list:
                    res.append(f'({a}, {b})')
        return res


test = Solution()
print(test.ambiguousCoordinates(s="(123)"))
print(test.ambiguousCoordinates(s="(00011)"))
print(test.ambiguousCoordinates(s="(0123)"))
print(test.ambiguousCoordinates(s="(100)"))
