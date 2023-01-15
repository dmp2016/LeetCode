from string import ascii_lowercase


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        d = dict((c, {c}) for c in ascii_lowercase)
        for ind in range(len(s1)):
            d[s1[ind]].add(s2[ind])
        sl = [{key}.union(d[key]) for key in d]

        while True:
            n = len(sl)
            for ind1 in range(n):
                for ind2 in range(ind1 + 1, n):
                    sn = sl[ind1].intersection(sl[ind2])
                    if sn:
                        sl[ind1].update(sl[ind2])
                        del sl[ind2]
                        break
                else:
                    continue
                break
            else:
                break
        dm = dict()
        for st in sl:
            me = min(st)
            for elem in st:
                dm[elem] = me
        
        return ''.join(map(lambda x: dm[x], baseStr))


test = Solution()
print(test.smallestEquivalentString(s1="parker", s2="morris", baseStr="parser"))
print(test.smallestEquivalentString(s1="hello", s2="world", baseStr="hold"))
print(test.smallestEquivalentString(
    s1="leetcode", s2="programs", baseStr="sourcecode"))
