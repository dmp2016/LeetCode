from typing import Optional, Tuple, Union
import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        self.res = 0
        def get_min_max(root: Optional[TreeNode]) -> Tuple[Optional[Union[int, float]], Optional[Union[int, float]]]:
            if not root:
                return math.inf, -math.inf
            left_min, left_max = get_min_max(root.left)
            right_min, right_max = get_min_max(root.right)
            children_min = min(left_min, right_min)
            children_max = max(left_max, right_max)
            if children_min < math.inf:
                self.res = max(self.res, abs(root.val - children_min))
            if children_max > -math.inf:
                self.res = max(self.res, abs(root.val - children_max))
            return min(children_min, root.val), max(children_max, root.val)

        get_min_max(root)
        return self.res


test = Solution()
root = TreeNode(8, TreeNode(3, None, None), TreeNode(5, None, None))
print(test.maxAncestorDiff(root))
