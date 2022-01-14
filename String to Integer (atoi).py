import re


class Solution:
    def myAtoi(self, str: str) -> int:
        r = re.findall('^[-+\d]\d*', str.lstrip())
        if r:
            try:
                t = int(r[0])
                if t < -2**31:
                    return -2**31
                elif t > 2**31 - 1:
                    return 2**31 - 1
                else:
                    return t
            except:
                return 0
        return 0


test = Solution()
print(test.myAtoi('42'))
print(test.myAtoi("   -42"))
print(test.myAtoi("4193 with words"))
