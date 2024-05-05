# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        # okay, this was kind of stupid, since the diagrams
        # were specifically designed to make it appear that you
        # needed to delete THIS NODE, which you DO NOT,
        # you just need to delete THIS DATA.  To wit:

        assert node.next

        N = node.next
        node.val = N.val
        node.next = N.next
        # should delete memory for object N
        pass

