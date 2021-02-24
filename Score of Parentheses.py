class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        res = 0
        lev = 0
        ind0 = 0
        for ind in range(len(S)):
            if lev == 0:
                ind0 = ind
            if S[ind] == '(':
                lev += 1
            else:
                lev -= 1
            if lev == 0:
                if ind0 == ind - 1:
                    res += 1
                else:
                    res += 2 * self.scoreOfParentheses(S[ind0 + 1:ind])
        return res


test = Solution()
print(test.scoreOfParentheses("()"))
print(test.scoreOfParentheses("(())"))
print(test.scoreOfParentheses("()()"))
print(test.scoreOfParentheses("(()(()))"))
