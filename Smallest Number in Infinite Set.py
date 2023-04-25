from heapq import heappop, heappush, heapify


class SmallestInfiniteSet:

    def __init__(self):
        self.q = [i for i in range(1, 10001)]
        self.data = set(self.q)
        heapify(self.q)

    def popSmallest(self) -> int:
        res = heappop(self.q)
        self.data.remove(res)
        return res

    def addBack(self, num: int) -> None:
        if num not in self.data:
            heappush(self.q, num)
            self.data.add(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)