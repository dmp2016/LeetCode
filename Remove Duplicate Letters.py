class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_ind = dict()
        for ind in range(len(s)):
            last_ind[s[ind]] = ind
        stack = []
        for ind in range(len(s)):
            c = s[ind]
            if c not in stack:
                while (stack and stack[-1] > c and last_ind[stack[-1]] > ind):
                    stack.pop()
                stack.append(c)
        return ''.join(stack)


test = Solution()
print(test.removeDuplicateLetters('bcabc'))
print(test.removeDuplicateLetters('cbacdcbc'))
