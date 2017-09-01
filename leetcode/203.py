# -*- encoding: utf-8 -*-
'''
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        while head != None and head.val == val:
            head = head.next

        p = head
        if head == None:
            return head

        q = p.next
        while q != None:
            if q.val == val:
                p.next = q.next
                q = q.next

            else:
                p = q
                q = q.next

        return head
