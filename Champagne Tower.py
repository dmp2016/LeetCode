class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        def get_limit(x: float) -> float:
            return x - 1 if x > 1 else 0

        a = [poured]
        for _ in range(query_row):
            b = []
            b.append(get_limit(a[0]) / 2)
            for ind in range(len(a) - 1):
                b.append((get_limit(a[ind]) + get_limit(a[ind + 1])) / 2)
            b.append(get_limit(a[-1]) / 2)
            a = b
        return a[query_glass] if a[query_glass] < 1 else 1


test = Solution()
print(test.champagneTower(poured=1, query_row=1, query_glass=1))
print(test.champagneTower(poured=2, query_row=1, query_glass=1))
print(test.champagneTower(poured=100000009, query_row=33, query_glass=17))
