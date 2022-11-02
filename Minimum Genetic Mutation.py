from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        front = {start}
        used = {start}
        depth  = 0
        while front:
            if end in front:
                return depth
            new_front = set()
            for cur_front in front:
                for item in bank:
                    if item not in used and sum(a != b for a, b in zip(item, cur_front)) == 1:
                        new_front.add(item)
            used.update(new_front)
            front = new_front
            depth += 1
        return -1


test = Solution()
print(test.minMutation(start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]))
print(test.minMutation(start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]))
print(test.minMutation(start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]))
