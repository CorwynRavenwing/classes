class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        def find(repDict: dict[int,int], node: int) -> int:
            rep = repDict[node]
            if node == rep:
                return node
            else:
                rep = find(repDict, rep)
                repDict[node] = rep
                return rep

        def countGroups(repDict: dict[int,int]) -> int:
            counts = Counter()
            for i in range(1, n + 1):
                rep = find(repDict, i)
                counts[rep] += 1
            print(f'countGroups() found {counts=}')
            return len(counts)
        
        def combineGroups(repDict: dict[int,int], u: int, v: int) -> int:
            u = find(repDict, u)
            v = find(repDict, v)
            if u == v:
                return False
            
            repDict[u] = v
            return True

        def edges_of_type(typeID: int) -> List[List[int]]:
            nonlocal edges
            return [
                (u, v)
                for (typeI, u, v) in edges
                if typeI == typeID
            ]

        representative = {
            i: i
            for i in range(1, n + 1)
        }
        print(f'{representative=}')
        
        deleted = 0
        # Step 1: add type-three edges
        for (u, v) in edges_of_type(3):
            changes = combineGroups(representative, u, v)
            if not changes:
                print(f'Edge 3:({u},{v}) unneeded')
                deleted += 1
        
        # Step 2: add type-one edges
        AliceRep = representative.copy()
        for (u, v) in edges_of_type(1):
            changes = combineGroups(AliceRep, u, v)
            if not changes:
                print(f'Edge 1:({u},{v}) unneeded')
                deleted += 1
        
        # Step 3: add type-two edges
        BobRep = representative.copy()
        for (u, v) in edges_of_type(2):
            changes = combineGroups(BobRep, u, v)
            if not changes:
                print(f'Edge 2:({u},{v}) unneeded')
                deleted += 1

        AliceGroups = countGroups(AliceRep)
        BobGroups = countGroups(BobRep)
        print(f'{AliceGroups=} {BobGroups=}')
        if AliceGroups == 1 and BobGroups == 1:
            return deleted
        else:
            return -1

