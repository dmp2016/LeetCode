from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        c = 0
        res, cur = None, None
        while l1 is not None or l2 is not None or c > 0:
            sm = c
            if l1 is not None:
                sm += l1.val
                l1 = l1.next
            if l2 is not None:
                sm += l2.val
                l2 = l2.next
            c = sm // 10
            l3 = ListNode(sm % 10, None)
            if res is None:
                res = l3
                cur = res
            else:
                cur.next = l3
                cur = l3
        return res


def convert_to_list_node(lst: List) -> ListNode:
    res = None
    for val in lst[::-1]:
        node = ListNode(val, res)
        res = node
    return res


def print_list_node(lst: ListNode):
    while lst is not None:
        print(lst.val, end=' ')
        lst = lst.next
    print()


A = convert_to_list_node([2, 4, 5])
print_list_node(A)
B = convert_to_list_node([5, 6, 4, 1])
print_list_node(B)
test = Solution()
print_list_node(test.addTwoNumbers(A, B))

