class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        q = []
        for c in s:
            if q and q[-1][0] == c:
                q[-1][1] += 1
                if q[-1][1] == k:
                    q[-1][1] -= k
                    if q[-1][1] == 0:
                        q.pop()
            else:
                q.append([c, 1])
        return ''.join([c * cnt for c, cnt in q])


test = Solution()
print(test.removeDuplicates(s="abcd", k=2))
print(test.removeDuplicates(s="deeedbbcccbdaa", k=3))
print(test.removeDuplicates(s="pbbcggttciiippooaais", k=2))
print(test.removeDuplicates(s="a", k=2))
