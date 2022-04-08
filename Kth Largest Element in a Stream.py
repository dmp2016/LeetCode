from sortedcontainers import SortedList


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.sl = SortedList(-n for n in nums)
        self.k = k
        
    def add(self, val: int) -> int:
        self.sl.add(-val)
        return -self.sl[self.k - 1]
