from typing import List
import math


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        store = {0: 0}
        for cur in range(1, amount + 1):
            store[cur] = min([store[cur - coin] + 1 for coin in coins if cur >= coin], default=math.inf)
        return -1 if store[amount] == math.inf else store[amount]


test = Solution()
print(test.coinChange(coins=[1, 2, 5], amount=11))
print(test.coinChange(coins=[2], amount=3))
print(test.coinChange(coins=[1], amount=0))
print(test.coinChange(coins=[1], amount=1))
print(test.coinChange(coins=[1], amount=2))
print(test.coinChange(coins=[1, 2, 5], amount=100))
