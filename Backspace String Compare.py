class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def transform_str(ss: str) -> str:
            sq = []
            for c in ss:
                if c != '#':
                    sq.append(c)
                elif sq:
                    sq.pop()
            return sq

        return transform_str(s) == transform_str(t)


test = Solution()
print(test.backspaceCompare(s="ab#c", t="ad#c"))
print(test.backspaceCompare(s="ab##", t="c#d#"))
print(test.backspaceCompare(s="a#c", t="b"))
