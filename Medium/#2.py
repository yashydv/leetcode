class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyhead = ListNode()
        curr = dummyhead
        carry = 0
        while(l1 != None or l2 != None):
            l1val = l1.val if l1 != None else 0
            l2val = l2.val if l2 != None else 0
            sum1 = carry + l1val + l2val
            carry = sum1//10
            curr.next = ListNode(sum1 % 10)
            curr = curr.next
            if (l1 != None): l1 = l1.next
            if (l2 != None): l2 = l2.next
            
        if carry > 0: curr.next = ListNode(carry)
        
        return dummyhead.next
