from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:

        def do_rec(n: int) -> TreeNode:
            if n == 0:
                return None
            nonlocal head
            a, b = n // 2, n - n // 2 - 1
            left = do_rec(a)
            val = head.val
            head = head.next
            right = do_rec(b)
            return TreeNode(val, left, right)

        tmp = head
        sz = 0
        while tmp:
            sz += 1
            tmp = tmp.next

        return do_rec(sz)


def array_to_list(list: List) -> ListNode:
    item = None
    for v in list[::-1]:
        item = ListNode(v, item)
    return item


test = Solution()
test.sortedListToBST(array_to_list([-10, -3, 0, 5, 9]))
test.sortedListToBST(array_to_list([]))
