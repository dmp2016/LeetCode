from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        head = prev
        res = 0
        m = 1
        while head:
            res += m * head.val
            m *= 2
            head = head.next
        return res


def array_to_list(list: List) -> ListNode:
    item = None
    for v in list[::-1]:
        item = ListNode(v, item)
    return item


test = Solution()
print(test.getDecimalValue(array_to_list([1, 0, 1])))
