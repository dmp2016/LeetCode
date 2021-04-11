# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        front = [root]
        while front:
            new_front = []
            for item in front:
                if item.left:
                    new_front.append(item.left)
                if item.right:
                    new_front.append(item.right)
            if not new_front:
                res = 0
                for item in front:
                    res += item.val
                return res
            front = new_front


test = Solution()
print(test.deepestLeavesSum(root=[1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8]))
print(test.deepestLeavesSum(root=[1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8]))
