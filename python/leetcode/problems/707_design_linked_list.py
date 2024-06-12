class Node:

    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
        return
    
class MyLinkedList:

    debug = False

    def __init__(self):
        self.HeadTailNode = Node(None, None, None)
        self.HeadTailNode.next = self.HeadTailNode
        self.HeadTailNode.prev = self.HeadTailNode
        self.count = 0
        return

    def show_list(self, label: str) -> None:
        if not self.debug:
            return
        node = self.HeadTailNode
        print(f"{label}: <H>", end=" ")
        node = node.next
        i = 0
        while node != self.HeadTailNode:
            print(f'[{i}]:{node.val}', end=" ")
            node = node.next
            i = i + 1
        print(f"<T> ({self.count})")
        return

    def node_at_index(self, index: int) -> Node:
        node = self.HeadTailNode
        node = node.next    # node 0, not head/tail
        if 0 <= index < self.count:
            for i in range(index):
                node = node.next
            return node
        else:
            print(f'{self.count=}: {index=} invalid')
            return None
        pass

    def get(self, index: int) -> int:
        self.show_list(f'get({index})')
        node = self.node_at_index(index)
        if node is None:
            print(f'  -> error, {-1}')
            return -1
        else:
            print(f'  -> value, {node.val}')
            return node.val

    def add_after_node(self, node: Node, val: int) -> None:
        nextNode = node.next
        newNode = Node(
            val,
            nextNode.prev,
            node.next,
        )
        nextNode.prev = newNode
        node.next = newNode
        self.count += 1
        return

    def add_before_node(self, node: Node, val: int) -> None:
        prevNode = node.prev
        self.add_after_node(prevNode, val)

    def addAtHead(self, val: int) -> None:
        self.show_list(f'before add@Head({val})')
        location = self.HeadTailNode
        self.add_after_node(location, val)
        self.show_list(f'after add@Head({val})')

    def addAtTail(self, val: int) -> None:
        self.show_list(f'before add@Tail({val})')
        location = self.HeadTailNode
        self.add_before_node(location, val)
        self.show_list(f'after add@Tail({val})')

    def addAtIndex(self, index: int, val: int) -> None:
        self.show_list(f'before add@Index([{index}],{val})')
        location = self.node_at_index(index)
        if location is None:
            if index > self.count:
                print(f'  -> error, no error message')
                return
            else:
                print(f'  -> index == count: add at end')
                location = self.HeadTailNode
                # fall through and perform the add
        self.add_before_node(location, val)
        self.show_list(f'after add@Index([{index}],{val})')
        return

    def delete_node(self, node: Node) -> None:
        if self.count <= 0:
            print("fail: no node to delete")
            return
        if node == self.HeadTailNode:
            print("fail: can't delete Head-Tail Node")
            return
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        self.count -= 1
        return

    def deleteAtIndex(self, index: int) -> None:
        self.show_list(f'before del@Index([{index}])')
        location = self.node_at_index(index)
        if location is None:
            print(f'  -> error, no error message')
            return
        else:
            self.delete_node(location)
            self.show_list(f'after del@Index([{index}])')

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
