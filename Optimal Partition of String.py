class Solution:
    def partitionString(self, s: str) -> int:
        cur = set()
        res = 1
        for c in s:
            if c in cur:
                cur.clear()
                res += 1
            cur.add(c)
        return res


t = Solution()
print(t.partitionString(s="abacaba"))
print(t.partitionString(s="ssssss"))
