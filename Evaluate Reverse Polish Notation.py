from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c in ['+', '-', '/', '*']:
                a = stack.pop()
                b = stack.pop()
                if c == '+':
                    stack.append(a + b)
                elif c == '-':
                    stack.append(b - a)
                elif c == '/':
                    stack.append(int(b / a))
                else:
                    stack.append(a * b)
            else:
                stack.append(int(c))
        return stack.pop()

test = Solution()
print(test.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))