# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        res = None
        tmp = headA
        while tmp is not None:
            tmp.val = -tmp.val
            tmp = tmp.next
        tmp = headB
        while tmp is not None:
            if tmp.val < 0:
                res = tmp
                break
            tmp = tmp.next
        tmp = headA
        while tmp is not None:
            tmp.val = -tmp.val
            tmp = tmp.next
        
        return res