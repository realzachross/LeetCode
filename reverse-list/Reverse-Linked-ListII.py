# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


test = ListNode(1, ListNode(2, ListNode(3, None)))


class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        beforeLeft, afterRight = head, head
        for i in range(right):
            afterRight = afterRight.next
            if i < left - 2:
                beforeLeft = beforeLeft.next
        if left == 1:
            beforeLeft = None
        if beforeLeft:
            l = beforeLeft.next
            beforeLeft.next = None
        else:
            l = head
        prev = None
        while l and l != afterRight:
            temp = l.next
            l.next = prev
            prev = l
            l = temp
        head2 = head
        while head2 and head2.next:
            head2 = head2.next
        if left == 1:
            head = head2 = prev
        else:
            head2.next = prev
        while prev and prev.next:
            prev = prev.next
        prev.next = afterRight
        return head


s = Solution()

l = Solution.reverseBetween(s, test, 1, 3)

while l:
    print(l.val)
    l = l.next
