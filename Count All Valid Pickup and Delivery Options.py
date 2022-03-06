class Solution:
    def countOrders(self, n: int) -> int:
        c = 1
        for k in range(1, n):
            r = 2 * k + 1
            c = (c * (r + 1) * r // 2) % 1000000007
        return c


test = Solution()
print(test.countOrders(10))
