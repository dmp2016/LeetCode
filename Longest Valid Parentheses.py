class Solution:
    def longestValidParentheses_slow(self, s: str) -> int:
        res = 0
        cur = 0
        d = {0: -1}
        for ind in range(len(s)):
            c = s[ind]
            if c == ')':
                cur -= 1
                if cur < 0:
                    cur = 0
                    d = {0: ind}
                else:
                    if cur in d:
                        res = max(res, ind - d[cur])
            else:
                cur += 1
                d[cur] = ind
        return res

    def longestValidParentheses(self, s: str) -> int:
        res = 0
        q = [-1]
        for ind in range(len(s)):
            c = s[ind]
            if c == '(':
                q.append(ind)
            elif len(q) > 1:
                q.pop()
                res = max(res, ind - q[-1])
            else:
                q = [ind]
        return res


test = Solution()
print(test.longestValidParentheses(s=")("))
print(test.longestValidParentheses(s="(()"))
print(test.longestValidParentheses(s=")()())"))
print(test.longestValidParentheses(s=")()))()())"))
print(test.longestValidParentheses(s=""))
print(test.longestValidParentheses(s="()(()"))
print(test.longestValidParentheses(s="(()()"))
