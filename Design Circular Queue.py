class MyList:
    def __init__(self, val: int, next=None) -> None:
        self.val = val
        self.next = next


class MyCircularQueue:

    def __init__(self, k: int):
        self.max_size = k
        self.cur_size = 0
        self.last = None
        self.first = None

    def enQueue(self, value: int) -> bool:
        if self.max_size == self.cur_size:
            return False
        elem = MyList(value, self.last)
        if self.last:
            self.last.next = elem
        self.last = elem
        if self.cur_size == 0:
            self.first = self.last
        self.cur_size += 1
        return True

    def deQueue(self) -> bool:
        if self.cur_size > 0:
            self.first = self.first.next
            self.cur_size -= 1
            return True
        else:
            return False

    def Front(self) -> int:
        return self.first.val if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.last.val if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.cur_size == 0

    def isFull(self) -> bool:
        return self.cur_size == self.max_size


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(8)
param_1 = obj.enQueue(3)
param_1 = obj.enQueue(9)
param_1 = obj.enQueue(5)
param_1 = obj.enQueue(0)
param_2 = obj.deQueue()
param_2 = obj.deQueue()
param_3 = obj.Front()
param_4 = obj.Rear()
param_5 = obj.isEmpty()
param_6 = obj.isFull()