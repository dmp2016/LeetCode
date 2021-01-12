class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def check_node(node: TreeNode):
            if node:
                if node.val == target.val:
                    return node
                child = check_node(node.left)
                if child:
                    return child
                child = check_node(node.right)
                if child:
                    return child
            return None
        return check_node(cloned)

