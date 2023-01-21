from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def check_part(part: str) -> bool:
            return len(part) > 0 and (len(part) == 1 or len(part) > 1 and part[0] != '0') and len(part) <= 3 and int(part) <= 255

        res = []
        for ind1 in range(1, len(s) - 2):
            c1 = s[:ind1]
            if not check_part(c1):
                continue
            for ind2 in range(ind1 + 1, len(s) - 1):
                c2 = s[ind1:ind2]
                if not check_part(c2):
                    continue
                for ind3 in range(ind2 + 1, len(s)):
                    c3 = s[ind2:ind3]
                    c4 = s[ind3:]
                    if check_part(c3) and check_part(c4):
                        res.append(f'{c1}.{c2}.{c3}.{c4}')
        return res


test = Solution()
# print(test.restoreIpAddresses(s="25525511135"))
print(test.restoreIpAddresses(s="0000"))
print(test.restoreIpAddresses(s="101023"))
