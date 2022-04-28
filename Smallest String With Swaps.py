from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        graph = dict()
        for pair in pairs:
            graph.setdefault(pair[0], set()).add(pair[1])
            graph.setdefault(pair[1], set()).add(pair[0])

        set_v = set(a[0] for a in pairs).union(a[1] for a in pairs)
        components = []
        while set_v:
            component = set()
            q = [set_v.pop()]
            while q:
                v = q.pop()
                component.add(v)
                for w in graph[v]:
                    if w not in component:
                        q.append(w)
            components.append(component)
            set_v.difference_update(component)

        opt_str = []
        comp_ind = dict()
        for num, comp in enumerate(components):
            opt_str.append(list(sorted([s[ind] for ind in comp], key=lambda x: -ord(x))))
            for ind in comp:
                comp_ind[ind] = num

        res = ''
        for ind in range(len(s)):
            if ind in comp_ind:
                res += opt_str[comp_ind[ind]].pop()
            else:
                res += s[ind]
        return res


test = Solution()
print(test.smallestStringWithSwaps(s="dcab", pairs=[[0, 3], [1, 2]]))
print(test.smallestStringWithSwaps(s="dcab", pairs=[[0, 3], [1, 2], [0, 2]]))
print(test.smallestStringWithSwaps(s="cba", pairs=[[0, 1], [1, 2]]))
