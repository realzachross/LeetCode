def reverseBetween(self, head, left, right):
    """
    :type head: ListNode
    :type left: int
    :type right: int
    :rtype: ListNode
    """
    dummy = ListNode(0, head)
    beforeLeft, afterRight = dummy, dummy
    for i in range(right + 1):
        afterRight = afterRight.next
        if i < left - 1:
            beforeLeft = beforeLeft.next
    prev, cur, exitCond = afterRight, beforeLeft.next, afterRight
    while cur and cur != exitCond:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    beforeLeft.next = prev
    return dummy.next
