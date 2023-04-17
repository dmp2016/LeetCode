from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_value = max(candies)
        return [val + extraCandies >= max_value for val in candies]
