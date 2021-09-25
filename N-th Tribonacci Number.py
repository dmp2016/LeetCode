class Solution:
    def tribonacci(self, n: int) -> int:
        A = [0, 1, 1]
        for i in range(3, n + 1):
            A.append(A[i - 1] + A[i - 2] + A[i - 3])
        return A[n]


test = Solution()
print(test.tribonacci(n=4))
print(test.tribonacci(n=25))
