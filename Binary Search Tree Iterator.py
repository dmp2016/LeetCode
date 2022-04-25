# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    @staticmethod
    def do_iter(node: TreeNode):
        if node is None:
            return []
        for item in BSTIterator.do_iter(node.left):
            yield item
        yield node
        for item in BSTIterator.do_iter(node.right):
            yield item        


    def __init__(self, root: Optional[TreeNode]):
        self.cust_iter = self.do_iter(root)
        self.cur = self.cust_iter.__next__()


    def next(self) -> int:
        res = self.cur.val
        try:
            self.cur = self.cust_iter.__next__()
        except:
            self.cur = None
        return res

    def hasNext(self) -> bool:
        return self.cur is not None
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
