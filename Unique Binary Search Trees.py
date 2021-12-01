class Solution:
    def numTrees(self, n: int) -> int:
        p = [1, 1]
        for k in range(2, n + 1):
            p.append(0)
            for up in range(1, k + 1):
                p[-1] += p[up - 1] * p[k - up]
        return p[-1]


test = Solution()
# print(test.numTrees(1))
print(test.numTrees(3))
print(test.numTrees(5))
print(test.numTrees(10))