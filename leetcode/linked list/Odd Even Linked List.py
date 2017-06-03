"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking
about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # my solution
        if not head:
            return
        count = 1
        odd ,even = [], []
        while head:
            next_node = head.next
            if count % 2 == 1:
                odd.append(head)
            else:
                even.append(head)
            head = next_node
        all_nodes = odd + even
        res = all_nodes[0]
        for i,node in enumerate(all_nodes):
            if i + 1 < len(all_nodes):
                node.next = all_nodes[i+1]
            if i == (len(all_nodes) - 1):
                node.next = None
        return res

    def oddEvenList2(self,head):
        # correct solution
        if head:
            odd = head
            even = head.next
            even_head = even
            while (even and even.next):
                odd.next = even.next
                even.next = even.next.next
                odd = odd.next
                even = even.next
            odd.next = even_head
        return head