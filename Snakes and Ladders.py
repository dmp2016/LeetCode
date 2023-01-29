from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        fld = []
        for ind in range(len(board)):
            k = len(board) - ind - 1
            if ind & 1:
                fld += board[k][::-1]
            else:
                fld += board[k]

        if len(fld) == 1:
            return 0
        res = 0
        front = {0}
        used = {0}
        while front:
            res += 1
            new_front = set()
            for a in front:
                for d in range(1, 7):
                    if (r := d + a) < len(fld):
                        if fld[r] == -1 and r not in used:
                            if r == len(fld) - 1:
                                return res
                            new_front.add(r)
                        elif (r1 := fld[r] - 1) not in used:
                            if r1 == len(fld) - 1:
                                return res
                            new_front.add(r1)
            used.update(new_front)
            front = new_front
        return -1


test = Solution()
print(test.snakesAndLadders(board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))
print(test.snakesAndLadders(board = [[-1,-1],[-1,3]]))
