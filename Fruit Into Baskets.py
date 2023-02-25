from typing import List
from collections import Counter


class Solution:
    def totalFruit1(self, fruits: List[int]) -> int:
        left, right = 1, len(fruits) + 1
        while left < right - 1:
            md = (left + right) // 2
            cn = Counter(fruits[:md])
            ind = 0
            while True:
                if len(cn) <= 2:
                    left = md
                    break
                if ind + md == len(fruits):
                    right = md
                    break
                else:
                    cn[fruits[ind]] -= 1
                    if cn[fruits[ind]] == 0:
                        del cn[fruits[ind]]
                    cn[fruits[ind + md]] += 1
                    ind += 1
        return left

    def totalFruit(self, fruits: List[int]) -> int:
        cnt = {fruits[0]: 1}
        ind1 = 0
        res = 1
        for ind2 in range(1, len(fruits)):
            cnt[fruits[ind2]] = cnt.get(fruits[ind2], 0) + 1
            while len(cnt) > 2:
                cnt[fruits[ind1]] -= 1
                if cnt[fruits[ind1]] == 0:
                    del cnt[fruits[ind1]]
                ind1 += 1
            res = max(res, ind2 - ind1 + 1)
        return res


test = Solution()
print(test.totalFruit1(fruits=[1, 2, 1]))
print(test.totalFruit(fruits=[1, 2, 1]))

print(test.totalFruit1(fruits=[0, 1, 2, 2]))
print(test.totalFruit(fruits=[0, 1, 2, 2]))

print(test.totalFruit1(fruits=[1, 2, 3, 2, 2]))
print(test.totalFruit(fruits=[1, 2, 3, 2, 2]))

print(test.totalFruit1(fruits=[0]))
print(test.totalFruit(fruits=[0]))

print(test.totalFruit1(fruits=[1, 1]))
print(test.totalFruit(fruits=[1, 1]))

print(test.totalFruit1(fruits=[0, 1, 1]))
print(test.totalFruit(fruits=[0, 1, 1]))

print(test.totalFruit1(fruits=[3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
print(test.totalFruit(fruits=[3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
