# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res = []
        front = [root]
        while True:
            front1 = []
            s = 0
            cnt = 0
            for item in front:
                s += item.val
                cnt += 1
                if item.left:
                    front1.append(item.left)
                if item.right:
                    front1.append(item.right)
            front = front1
            if cnt > 0:
                res.append(s / cnt)
            else:
                break
        return res