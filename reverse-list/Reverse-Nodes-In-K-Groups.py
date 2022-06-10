class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SolutionRecursive(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def helper(head, k):
            lead = head
            for i in range(k - 1):
                if lead and lead.next:
                    lead = lead.next
                else:
                    return head
            prev, cur = helper(lead.next, k), head
            for i in range(k):
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            return prev

        return helper(head, k) if k > 1 else head


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head
        dummy, cur, inc = ListNode(0, head), head, 0
        dummy2 = dummy
        while True:
            lead = cur
            for i in range(k - 1):
                if lead and lead.next:
                    lead = lead.next
                    if inc > 0:
                        dummy2 = dummy2.next
                else:
                    return dummy.next
            prev = lead.next
            for i in range(k):
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            dummy2.next = prev
            dummy2 = dummy2.next
            inc += 1
        return dummy.next
