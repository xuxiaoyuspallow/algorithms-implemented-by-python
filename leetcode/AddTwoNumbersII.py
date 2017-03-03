# coding:utf-8
"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit
comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1)
            l1 = l1.next
        while l2:
            stack2.append(l2)
            l2 = l2.next
        res = cur = ListNode(0)
        carry = 0
        while stack1 or stack2 or carry:
            if stack1:
                l1 = stack1.pop()
                carry += l1.val
            if stack2:
                l2 = stack2.pop()
                carry += l2.val
            cur.next = ListNode(carry % 10)
            cur = cur.next
            carry //= 10
        return self.reverse_linked_list(res.next)

    def reverse_linked_list(self,linked_list):
        the_next, the_last = None, None
        while linked_list:
            the_next = linked_list.next
            linked_list.next = the_last
            the_last = linked_list
            linked_list = the_next
        return the_last
