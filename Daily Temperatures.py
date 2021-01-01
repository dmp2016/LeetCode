from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = [0]
        res = [0] * len(T)
        ind = 1
        while ind < len(T):
            while stack and T[stack[-1]] < T[ind]:
                res[stack[-1]] = ind - stack[-1]
                stack.pop()
            stack.append(ind)
            ind += 1
        return res
        

test = Solution()
print(test.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
