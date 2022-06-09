# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if (not head) or (not head.next):
            return head
        temp, ln = head, 0
        while temp:
            temp = temp.next
            ln += 1
        rotations = k % ln
        if rotations == 0:
            return head
        toNewHead, last = head, head
        for i in range(rotations):
            last = last.next
        while last and last.next:
            last = last.next
            toNewHead = toNewHead.next
        newHead = toNewHead.next
        toNewHead.next = None
        last.next = head
        return newHead
