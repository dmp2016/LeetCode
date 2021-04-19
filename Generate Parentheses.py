from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:        
        sets = [set() for _ in range(n + 1)]
        sets[0] = set([''])
        for i in range(1, n + 1):
            for j in range(1, i):
                sets[i].update([s1 + s2 for s1 in sets[i - j] for s2 in sets[j]])
            for s in sets[i - 1]:
                sets[i].add('(' + s + ')')
        return list(sets[-1])


test = Solution()
print(test.generateParenthesis(3))
print(test.generateParenthesis(2))
print(test.generateParenthesis(1))
