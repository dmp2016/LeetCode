class Solution:
    def isValid(self, s: str) -> bool:
        queue = []
        cl = {'[': ']', '(': ')', '{': '}'}
        for c in s:
            if c in {'[', '(', '{'}:
                queue.append(c)
            elif not queue or cl[queue[-1]] != c:
                return False
            else:
                queue.pop()
        return len(queue) == 0


test = Solution()
print(test.isValid(s = "()"))
print(test.isValid(s = "()[]{}"))
print(test.isValid(s = "(]"))
print(test.isValid(s = "([)]"))
print(test.isValid(s = "([)]"))
print(test.isValid(s = "{[]}"))
