from typing import List


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        
        def check(s1: str, s2: str):
            difs = []
            if s1 == s2:
                return True
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    if len(difs) > 2:
                        return False
                    difs.append((c1, c2))
            if len(difs) == 2 and difs[0][0] == difs[1][1] and difs[0][1] == difs[1][0]:
                return True
            else:
                return False
        
        not_visited = set(s for s in strs)
        res = 0
        for start in strs:
            if start in not_visited:
                q = [start]
                while q:
                    cur = q.pop()                    
                    if cur in not_visited:
                        not_visited.remove(cur)
                        for str_next in not_visited:
                            if check(cur, str_next):
                                q.append(str_next)
                res += 1
        return res


t = Solution()
print(t.numSimilarGroups(strs=["tars", "rats", "arts", "star"]))
print(t.numSimilarGroups(strs=["omv", "ovm"]))
