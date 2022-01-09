class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos_set = set()
        cur = [0, 0]
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        cur_dir = 0
        for _ in range(5):
            pos_len = len(pos_set)
            for step in instructions:
                pos_set.add(tuple(cur))
                if step == 'G':
                    cur[0], cur[1] = cur[0] + dirs[cur_dir][0], cur[1] + dirs[cur_dir][1]
                elif step == 'L':
                    cur_dir -= 1
                    cur_dir %= 4
                else:
                    cur_dir += 1
                    cur_dir %= 4
            if pos_len == len(pos_set):
                return True
        return False


test = Solution()
print(test.isRobotBounded("GGLLGG"))
print(test.isRobotBounded("GG"))
print(test.isRobotBounded("GL"))
