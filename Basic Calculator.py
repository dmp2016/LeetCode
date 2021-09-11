from collections import deque
from enum import Enum
from typing import Optional


class Solution:
    def calculate(self, s: str) -> int:
        self.cur_pos = 0

        def do() -> int:
            operands = deque()
            opers = deque()
            while True:
                if self.cur_pos == len(s) or s[self.cur_pos] == ')':
                    if operands:
                        res = operands.popleft()
                        while operands:
                            b = operands.popleft()
                            oper = opers.popleft()
                            if oper == '+':
                                res += b
                            else:
                                res -= b
                        if self.cur_pos < len(s):
                            self.cur_pos += 1
                        return res
                if s[self.cur_pos].isdecimal():
                    old_cur_pos = self.cur_pos
                    while self.cur_pos < len(s) and s[self.cur_pos].isdecimal():
                        self.cur_pos += 1
                    operands.append(int(s[old_cur_pos:self.cur_pos]))
                elif s[self.cur_pos] == '(':
                    self.cur_pos += 1
                    operands.append(do())
                else:
                    opers.append(s[self.cur_pos])
                    if len(operands) < len(opers):
                        operands.append(0)
                    self.cur_pos += 1

        s = ''.join([c for c in s if c != ' '])
        return do()


test = Solution()
# print(test.calculate(s="-1+5"))
print(test.calculate(s="1+(4+5+2)-3"))

print(test.calculate(s="1 + 1"))
print(test.calculate(s=" 2-1 + 2 "))
print(test.calculate(s="(1+(4+5+2)-3)+(6+8)"))
