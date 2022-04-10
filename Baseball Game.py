from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        st = []
        for s in ops:
            if s == "C":
                st.pop()
            elif s == "D":
                st.append(st[-1] * 2)
            elif s == "+":
                st.append(st[-1] + st[-2])
            else:
                st.append(int(s))
        return sum(st)


test = Solution()
print(test.calPoints(ops=["5", "2", "C", "D", "+"]))
print(test.calPoints(ops=["5", "-2", "4", "C", "D", "9", "+", "+"]))
