from typing import List
import math
import sys

sys.setrecursionlimit(100000)


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def get_next(cur: str, num: int) -> str:
            res = ''
            for i in range(4):
                if i == num:
                    c = str(int(cur[num]) + 1)
                    if c == '10':
                        c = '0'
                else:
                    c = cur[i]
                res += c
            return res

        def get_prev(cur: List[str], num: int) -> str:
            res = ''
            for i in range(4):
                if i == num:
                    c = str(int(cur[num]) - 1)
                    if c == '-1':
                        c = '9'
                else:
                    c = cur[i]
                res += c
            return res

        deadends = set(deadends)

        if '0000' in deadends:
            return -1
        front = ['0000']
        found = set()
        cnt = 0
        while front:
            if target in front:
                return cnt
            found.update(front)
            cnt += 1
            new_front = set()
            for a in front:
                for i in range(4):
                    b = get_next(a, i)
                    if b not in found and b not in deadends:
                        new_front.add(b)
                    b = get_prev(a, i)
                    if b not in found and b not in deadends:
                        new_front.add(b)
            front = new_front

        return -1


test = Solution()
print(test.openLock(deadends=["0001"], target="1000"))
print(test.openLock(deadends=["0201", "0101", "0102", "1212", "2002"], target="0202"))
print(test.openLock(deadends=["8888"], target="0009"))
print(test.openLock(deadends=["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], target="8888"))
print(test.openLock(deadends=["0000"], target="8888"))
