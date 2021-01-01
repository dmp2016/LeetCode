from heapq import heappush, heappop
from collections import defaultdict


class FreqStack:

    def __init__(self):
        self.heap = []
        self.elem_nums = defaultdict(int)
        self.stack_cnt = 0

    def push(self, x: int) -> None:
        self.stack_cnt += 1
        self.elem_nums[x] += 1
        heappush(self.heap, (-self.elem_nums[x], -self.stack_cnt, x))

    def pop(self) -> int:
        _, _, x = heappop(self.heap)
        self.elem_nums[x] -= 1
        return x


test = FreqStack()
test.push(5)
test.push(7)
test.push(5)
test.push(7)
test.push(4)
test.push(5)
print(test.pop())
print(test.pop())
print(test.pop())
print(test.pop())
print(test.pop())
