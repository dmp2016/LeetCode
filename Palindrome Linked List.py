from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        tmp = head
        n = 0
        while tmp:
            tmp = tmp.next
            n += 1

        tmp = head
        prev = None
        for _ in range(n//2):
            prev, tmp.next, tmp  = tmp, prev, tmp.next
        
        head1 = prev
        head2 = tmp.next if n & 1 else tmp
        while head1:
            if head1.val != head2.val:
                return False
            head1 = head1.next
            head2 = head2.next
        return True


def array_to_list(list: List) -> ListNode:
    item = None
    for v in list[::-1]:
        item = ListNode(v, item)
    return item


def print_list(head: ListNode):
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    print()


test = Solution()
print(test.isPalindrome(array_to_list([1, 3, 1])))
print(test.isPalindrome(array_to_list([1, 2, 2, 1])))
print(test.isPalindrome(array_to_list([1, 1])))
print(test.isPalindrome(array_to_list([1])))
