class MyCalendar:

    def __init__(self):
        self.data = []

    def book(self, start: int, end: int) -> bool:
        for a, b in self.data:
            if start < b and end > a:
                return False
        self.data.append((start, end))
        return True


test = MyCalendar()
print([test.book(a, b) for a, b in [[47,50],[33,41],[25,32],[19,25]]])


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)