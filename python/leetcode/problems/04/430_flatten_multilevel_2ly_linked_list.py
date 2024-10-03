"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # SHORTCUT: since we're always splicing the "child" links into the
        # "next" link, we never actually change the head itself.  Therefore
        # when we finish, we can always just return "head"

        node = head
        while node:
            # if no child, there's nothing to do for this node
            if node.child:
                Child = self.flatten(node.child)
                node.child = None
                Next = node.next
                node.next = Child
                if node.next:
                    node.next.prev = node   # fix reverse link
                while node and node.next:
                    # skip forward to end of Child section
                    node = node.next
                node.next = Next
                if node.next:
                    node.next.prev = node   # fix reverse link
                # splice old Next onto end of Child
            node = node.next
            # step into old Next node
        
        return head

# NOTE: Accepted on first Submit
# NOTE: Runtime 42 ms Beats 20.97%
# NOTE: Memory 17.20 MB Beats 21.62%
