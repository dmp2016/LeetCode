# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        res = head
        ind = 1
        a = dict()
        while head:
            a[ind] = head
            ind += 1
            head = head.next
        a[k].val, a[len(a) - k + 1].val = a[len(a) - k + 1].val, a[k].val
        return res
