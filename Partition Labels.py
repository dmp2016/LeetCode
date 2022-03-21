from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        inds = dict()
        for ind in range(len(s)):
            inds[s[ind]] = ind
        res = [-1]
        ind = 0
        right = 0
        while ind < len(s):
            right = max(right, inds[s[ind]])
            if right <= ind:
                res.append(right)
            ind += 1
        return [res[ind + 1] - res[ind] for ind in range(len(res) - 1)]


test = Solution()
print(test.partitionLabels(s="ababcbacadefegdehijhklij"))
print(test.partitionLabels(s="eccbbbbdec"))
