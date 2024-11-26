class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.parentOf = {}
        self.childrenOf = {}
        self.dead = set()
        return

    def birth(self, parentName: str, childName: str) -> None:
        self.parentOf[childName] = parentName
        self.childrenOf.setdefault(parentName, [])
        self.childrenOf[parentName].append(childName)
        return

    def death(self, name: str) -> None:
        self.dead.add(name)
        return

    def getInheritanceOrder(self) -> List[str]:

        curOrder_list = []
        curOrder_set = set()
        def Successor(x: str) -> str:
            # print(f'S({x}):')
            nonlocal curOrder_list
            nonlocal curOrder_set
            if x in self.childrenOf:
                for child in self.childrenOf[x]:
                    if child not in curOrder_set:
                        # print(f'  -> {child}')
                        return child
            # no children, or ran out of children
            if x == self.king:
                # print(f'  -> {None}')
                return None
            else:
                # print(f'  -> (recurse)')
                return Successor(self.parentOf[x])

        person = self.king
        while person:
            curOrder_list.append(person)
            curOrder_set.add(person)
            person = Successor(person)
        
        # print(f'{curOrder_list=}')

        not_dead = [
            person
            for person in curOrder_list
            if person not in self.dead
        ]

        return not_dead

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

# NOTE: Accepted on second Run (needed a .setdefault)
# NOTE: Accepted on second Submit (Time Limit Exceeded)
# NOTE: Runtime 163 ms Beats 30.48%
# NOTE: Memory 74.28 MB Beats 5.52%
