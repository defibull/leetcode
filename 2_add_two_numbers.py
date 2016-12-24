def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr = ListNode(0)
        result = curr
        sum = 0
        while l1 or l2:
            sum = sum/10 #becomes carry
            if l1:
                sum+=l1.val
                l1 = l1.next
            if l2:
                sum+=l2.val
                l2 = l2.next
            curr.next = ListNode(sum%10)
            curr = curr.next
        if sum/10 == 1:
            curr.next = ListNode(1)
        return result.next
