class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = ''
        state = 0
        for c in s:
            if c == '(':
                state += 1
            elif c == ')':
                if state > 0:
                    state -= 1
                else:
                    continue
            res += c
        while state > 0:
            ind = res.rfind('(')
            res = res[:ind] + res[ind + 1:]
            state -= 1
        return res


test = Solution()
print(test.minRemoveToMakeValid(s="lee(t(c)o)de)"))
print(test.minRemoveToMakeValid(s="a)b(c)d"))
print(test.minRemoveToMakeValid(s="))(("))
print(test.minRemoveToMakeValid(s="(a(b(c)d)"))
