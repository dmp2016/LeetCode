class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        if X >= Y:
            return X - Y
        else:
            return 2 + self.brokenCalc(X, (Y + 1) // 2) if Y & 1 else 1 + self.brokenCalc(X, Y // 2)


test = Solution()
print(test.brokenCalc(X=2, Y=3))
print(test.brokenCalc(X=5, Y=8))
print(test.brokenCalc(X=3, Y=10))
print(test.brokenCalc(X=1024, Y=1))
