# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # fake start
        Dummy = ListNode(0)
        # head is the current node, move it till end(nullptr)
        while head is not None:
            # the processing node
            ptr = head
            # move head
            head = head.next
            # insertion place
            pos = Dummy
            # move insertion place when next node is not None and smaller than it
            while pos.next is not None and pos.next.val < ptr.val:
                pos = pos.next
            # pos->ptr->pos.next
            ptr.next = pos.next
            pos.next = ptr
        return Dummy.next
        