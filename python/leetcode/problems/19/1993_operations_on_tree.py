class LockingTree:

    def __init__(self, parent: List[int]):
        self.nodeParent = {}
        self.nodeChildren = {}
        self.nodeLockedBy = {}
        for childId, parentId in enumerate(parent):
            if parentId == -1:
                parentId = None
            self.nodeParent[childId] = parentId
            self.nodeChildren.setdefault(parentId, [])
            self.nodeChildren[parentId].append(childId)
        # print(f'{self.nodeParent=}')
        # print(f'{self.nodeChildren=}')
        # print(f'{self.nodeLockedBy=}')

    def node_is_locked(self, num: int) -> bool:
        return num in self.nodeLockedBy

    def node_is_unlocked(self, num: int) -> bool:
        return not self.node_is_locked(num)

    def any_ancestor_is_locked(self, num: int) -> bool:
        # print(f'AAIL({num}):')
        parent = self.nodeParent[num]
        if parent is None:
            # print(f'  Ran out of ancestors')
            return False
        elif self.node_is_locked(parent):
            # print(f'  {parent=} is locked')
            return True
        else:
            # print(f'  check {parent=}')
            return self.any_ancestor_is_locked(parent)

    def any_descendent_is_locked(self, num: int) -> bool:
        # print(f'ADIL({num}):')
        if num in self.nodeChildren:
            children = self.nodeChildren[num]
            for child in children:
                if self.node_is_locked(child):
                    # print(f'  {child=} is locked')
                    return True
                else:
                    # print(f'  check {child=}')
                    if self.any_descendent_is_locked(child):
                        return True
        #     print(f'  Checked all children of {num}')
        # else:
        #     print(f'  Node {num} has no children')
        return False

    def lock(self, num: int, user: int) -> bool:
        if num not in self.nodeLockedBy:
            print(f'Locking node #{num} for {user=}')
            self.nodeLockedBy[num] = user
            return True
        else:
            print(f'FAIL: cannot lock node #{num} for {user=}.')
            print(f'  Node already locked by {self.nodeLockedBy[num]}')
            return False

    def unlock(self, num: int, user: int) -> bool:
        if num not in self.nodeLockedBy:
            print(f'FAIL: cannot unlock node #{num}: already unlocked')
            return False
        elif (locker := self.nodeLockedBy[num]) == user:
            print(f'Unlocking node #{num} for {user=}')
            del self.nodeLockedBy[num]
            return True
        else:
            print(f'FAIL: cannot unlock node #{num} for {user=}')
            print(f'  Locked by {locker}')
            return False

    def force_unlock(self, num: int) -> None:
        if num in self.nodeLockedBy:
            print(f'  FORCE UNLOCK {num} (locked by {self.nodeLockedBy[num]})')
            del self.nodeLockedBy[num]
        return

    def force_unlock_all_descendents(self, num: int) -> None:
        # print(f'FUAD({num}):')
        if num in self.nodeChildren:
            children = self.nodeChildren[num]
            for child in children:
                if self.node_is_locked(child):
                    # print(f'  Unlocking {child=}')
                    self.force_unlock(child)
                self.force_unlock_all_descendents(child)
        return

    def upgrade(self, num: int, user: int) -> bool:
        if self.node_is_locked(num):
            print(f'FAIL: Cannot upgrade {num}, node is locked')
            return False
        elif not self.any_descendent_is_locked(num):
            print(f'FAIL: Cannot upgrade {num}, has no locked descendents')
            return False
        elif self.any_ancestor_is_locked(num):
            print(f'FAIL: Cannot upgrade {num}, ancestor is locked')
            return False
        else:
            print(f'*** UPGRADE {num} for {user=}')
            self.force_unlock_all_descendents(num)
            return self.lock(num, user)

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
