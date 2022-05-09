from typing import List


class Node:
    def __init__(self, val: int, inds: List[int], next: "Node"=None):
        self.val = val
        self.inds = inds
        self.next = next


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        val_ind = sorted([(b, a) for a, b in enumerate(nums)], key=lambda x: (x[0], -x[1]))
        cur_node = Node(val_ind[0][0], [val_ind[0][1]])
        ind_map = {val_ind[0][0]: cur_node}
        for ind in range(1, len(val_ind)):
            if cur_node.val < val_ind[ind][0]:
                cur_node = Node(val_ind[ind][0], [val_ind[ind][1]], cur_node)
                ind_map[val_ind[ind][0]] = cur_node
            else:
                cur_node.inds.append(val_ind[ind][1])
        min_left = nums[0]
        for ind in range(1, len(nums) - 1):
            mid = nums[ind]
            node = ind_map[mid]
            if not node:
                continue
            node = node.next
            while node and node.val > min_left:
                while node.inds and node.inds[-1] < ind:
                    node.inds.pop()
                if node.inds:
                    return True
                node = node.next
            ind_map[mid].next = node
            min_left = min(nums[ind], min_left)
        return False


test = Solution()
print(test.find132pattern(nums=[1, 2, 3, 4]))
print(test.find132pattern(nums=[3, 1, 4, 2]))
print(test.find132pattern(nums=[-1, 3, 2, 0]))
print(test.find132pattern(nums=[1, 0, 1, -4, -3]))
