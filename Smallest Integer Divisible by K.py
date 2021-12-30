class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        cur = 1 % k
        res = 1
        rem_set = set()
        while cur:
            rem_set.add(cur)
            cur = (cur * 10 + 1) % k
            if cur in rem_set:
                return -1
            res += 1
        return res


test = Solution()
print(test.smallestRepunitDivByK(4))
print(test.smallestRepunitDivByK(1))
print(test.smallestRepunitDivByK(3))
print(test.smallestRepunitDivByK(2))
print(test.smallestRepunitDivByK(11111*17))
print(test.smallestRepunitDivByK(11111*17))
