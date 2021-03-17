from typing import List


class Solution:

    def maxProfit(self, prices: List[int], fee: int) -> int:
        store_a = dict()
        store_b = dict()

        def do_rec(is_a: bool, ind: int) -> int:
            if ind == len(prices):
                return 0
            if is_a:
                if ind in store_a:
                    return store_a[ind]
                store_a[ind] = max(prices[ind] + do_rec(False, ind + 1), do_rec(True, ind + 1))
                return store_a[ind]
            else:
                if ind in store_b:
                    return store_b[ind]
                store_b[ind] = max(- prices[ind] - fee + do_rec(True, ind + 1), do_rec(False, ind + 1))
                return store_b[ind]

        return max(do_rec(False, 0), 0)

    def maxProfit(self, prices: List[int], fee: int) -> int:
        a = prices[-1]
        b = 0

        for ind in range(1, len(prices)):
            a = max(prices[-ind - 1] + b, a)
            b = max(-prices[-ind - 1] - fee + a, b)

        return max(b, 0)


test = Solution()
print(test.maxProfit(prices=[1, 3, 2, 8, 4, 9], fee=2))
print(test.maxProfit(prices=[1, 3, 7, 5, 10, 3], fee=3))
