"""
 1 ==> 2 ==>4 ==> 5  to   5 ==> 4 ==> 2 ==> 1
"""


class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None


def reverse_list_iterative(head):
    rev = None
    while head:
        head.next, rev, head = rev, head, head.next
    return rev


if __name__ == '__main__':
    head = ListNode(1)
    node1 =ListNode(2)
    node2 = ListNode(4)
    node3 = ListNode(5)
    head.next = node1
    node1.next =node2
    node2.next = node3
    p = reverse_list_iterative(head)
    while p:
        print(p.val)
        p =p.next