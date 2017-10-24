# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # use two pointers
        ptr1 = ptr2 = head
        while ptr1 is not None and ptr1.next is not None:
            # 2 step / 1 step
            ptr1 = ptr1.next.next
            ptr2 = ptr2.next
            # if there's a loop, they will meet finally
            if ptr1 == ptr2:
                return True
        return False