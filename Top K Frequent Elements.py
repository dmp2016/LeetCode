from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [a[0] for a in Counter(nums).most_common(k)]

test = Solution()
print(test.topKFrequent([1,1,1,2,2,3], 2))
