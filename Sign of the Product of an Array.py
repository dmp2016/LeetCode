from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg_cnt = 0
        for a in nums:
            if a == 0:
                return 0
            elif a < 0:
                neg_cnt += 1
        return -1 if neg_cnt & 1 else 1
