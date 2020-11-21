from typing import List
import random
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def custom_sort(self, head: ListNode, n: int):
        if head is None:
            return None
        base_item = head
        for _ in range(1, random.randint(0, n - 1)):
            base_item = base_item.next
        base_tail = base_item
        head_left, head_right = None, None
        tmp = head
        n_left, n_right = 0, 0
        while (tmp is not None):
            tmp_next = tmp.next
            if tmp != base_tail:
                if tmp.val < base_item.val:
                    tmp.next = head_left
                    head_left = tmp
                    n_left += 1
                elif tmp.val > base_item.val:
                    tmp.next = head_right
                    head_right = tmp
                    n_right += 1
                else:
                    tmp.next = base_item
                    base_item = tmp
            tmp = tmp_next
        base_tail.next = self.custom_sort(head_right, n_right)
        if head_left is not None:
            head_left = self.custom_sort(head_left, n_left)
            tmp = head_left
            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = base_item
            return head_left
        else:
            return base_item

    def sortList(self, head: ListNode) -> ListNode:
        n = 0
        tmp = head
        while tmp is not None:
            n += 1
            tmp = tmp.next
        return self.custom_sort(head, n)


def array_to_list(list: List) -> ListNode:
    item = None
    for v in list[::-1]:
        item = ListNode(v, item)
    return item


def print_list(head: ListNode):
    while head is not None:
        print(head.val, end=' ')
        head = head.next


test = Solution()
head = array_to_list([3, 3, 3])
print_list(test.sortList(head))
print()

head = array_to_list([4, 2, 1, 3])
print_list(test.sortList(head))
print()

head = array_to_list([-1, 5, 3, 4, 0])
print_list(test.sortList(head))
print()

head = array_to_list([1] * 100000)
test.sortList(head)
print()

head = array_to_list(list(range(2, 50000)))
test.sortList(head)
print()
