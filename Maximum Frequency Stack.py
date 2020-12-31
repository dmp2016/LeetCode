from sortedcontainers import SortedList


class FreqStack:

    def __init__(self):
        self.orderer = SortedList()
        self.elem_nums = {}
        self.stack_cnt = 0

    def push(self, x: int) -> None:
        self.stack_cnt += 1
        if x in self.elem_nums:
            elem = (len(self.elem_nums[x]), self.elem_nums[x][-1], x)
            self.orderer.remove(elem)
            self.elem_nums[x].append(self.stack_cnt)
            elem = (len(self.elem_nums[x]), self.elem_nums[x][-1], x)
            self.orderer.add(elem)
        else:
            self.elem_nums[x] = [self.stack_cnt]
            elem = (len(self.elem_nums[x]), self.elem_nums[x][-1], x)
            self.orderer.add(elem)

    def pop(self) -> int:
        elem = self.orderer.pop()
        x = elem[2]
        self.elem_nums[x].pop()
        if len(self.elem_nums[x]) == 0:
            self.elem_nums.pop(x)
        else:
            self.orderer.add((len(self.elem_nums[x]), self.elem_nums[x][-1], x))
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
