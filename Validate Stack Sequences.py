from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if not pushed:
            return len(popped) == 0
        q = [pushed[0]]
        ind_push, ind_pop = 1, 0
        while True:
            if q and ind_pop < len(popped) and q[-1] == popped[ind_pop]:
                q.pop()
                ind_pop += 1
            elif ind_push < len(pushed):
                q.append(pushed[ind_push])
                ind_push += 1
            else:
                break
        return ind_pop == len(popped)


test = Solution()
print(test.validateStackSequences(pushed = [1,2,3,4,5], popped = [4,5,3,2,1]))
print(test.validateStackSequences(pushed = [1,2,3,4,5], popped = [4,3,5,1,2]))
print(test.validateStackSequences(pushed = [1,2,3,4,5], popped = []))
print(test.validateStackSequences(pushed = [], popped = []))
print(test.validateStackSequences(pushed = [], popped = [1]))

