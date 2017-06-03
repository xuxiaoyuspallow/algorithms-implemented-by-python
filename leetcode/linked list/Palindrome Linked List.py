"""
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # my solution O(n) time and O(n) space
        if not head:
            return True
        val_list = []
        while head:
            val_list.append(head.val)
            head = head.next
        for i in range(len(val_list)/2):
            if val_list[i] != val_list[len(val_list) - i -1]:
                return False
        return True

    def isPalindrome2(self,head):
        # O(n) time and O(1) space
        if not head:
            return True
        fast,slow = head, head
        while (fast and fast.next):
            fast = fast.next.next
            slow = slow.next
        if fast:
            slow = slow.next

        prev = None
        while slow:
            next_slow = slow.next
            slow.next = prev
            prev = slow
            slow = next_slow

        slow = prev
        while slow:
            if slow.val != head.val:
                return False
            slow = slow.next
            head = head.next
        return True