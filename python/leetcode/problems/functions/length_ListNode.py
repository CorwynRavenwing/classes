
        def length_ListNode(node: ListNode) -> int:
            length = 0
            while node:
                length += 1
                node = node.next
            return length

