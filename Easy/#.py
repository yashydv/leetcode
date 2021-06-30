class Solution:

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        start = ListNode(val=0)

        index = start

        while l1!=None or l2!=None:

            if l1 != None and (l2==None or l1.val <= l2.val):

                index.next = l1

                index = index.next

                l1 = l1.next

            elif l2 != None and (l1 == None or l1.val >= l2.val):

                index.next = l2

                index = index.next

                l2 = l2.next

        start = start.next

        print(start)

        return start
