import typing


from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        front = [root]
        right_side = [root.val]
        while True:
            new_front = []
            for node in front:
                if node.left:
                    new_front.append(node.left)
                if node.right:
                    new_front.append(node.right)
            if new_front:
                right_side.append(new_front[-1].val)
            else:
                break
            front = new_front
        return right_side


test = Solution()
