class Solution:
    def maximumInvitations(self, Favorites: List[int]) -> int:
        
        def maxChainLength(start: int, skip: List[int]) -> int:
            lengths = [
                1 + maxChainLength(neighbor, skip)
                for neighbor in Neighbors[start]
                if neighbor not in skip
            ]
            answer = max(lengths, default=0)
            return answer

        seen = set()
        neighborCount = None
        outdegreeZero = None
        outdegreeNonZero = None
        def deleteLeafChains() -> None:
            print(f'DLC()')
            nonlocal seen, neighborCount
            nonlocal outdegreeZero, outdegreeNonZero
            # print(f'(before) DEBUG: {Neighbors=}')
            while True:
                # print(f'(loop) DEBUG: {Neighbors=}')
                if neighborCount is None:
                    neighborCount = {
                        employee: len(neighborSet)
                        for employee, neighborSet in Neighbors.items()
                        if employee not in seen
                    }
                    print(f'  create neighborCount')
                print(f'  neighborCount: {len(neighborCount)}')
                
                if outdegreeZero is None:
                    outdegreeZero = {
                        employee
                        for employee, count in neighborCount.items()
                        if count == 0
                    }
                    print(f'  create outdegreeZero')
                print(f'  outdegreeZero: {len(outdegreeZero)}')

                if outdegreeNonZero is None:
                    outdegreeNonZero = {
                        employee
                        for employee, count in neighborCount.items()
                        if count != 0
                    }
                    print(f'  create outdegreeNonZero')
                print(f'  outdegreeNonZero: {len(outdegreeNonZero)}')

                if not outdegreeZero:
                    break
                if not neighborCount:
                    break

                deleted_anything = False
                for test in tuple(outdegreeZero):
                    if test in seen:
                        break
                    leaf = test
                    while True:
                        if leaf in seen:
                            break
                        else:
                            seen.add(leaf)
                        # print(f'  (del {leaf})')
                        deleted_anything = True
                        favorite = Favorites[leaf]
                        if leaf not in Neighbors[favorite]:
                            break
                        Neighbors[favorite].remove(leaf)
                        neighborCount[favorite] -= 1
                        assert neighborCount[favorite] >= 0
                        if neighborCount[favorite] == 0:
                            outdegreeZero.add(favorite)
                            outdegreeNonZero.remove(favorite)
                            leaf = favorite
                        else:
                            break
                if not deleted_anything:
                    break
            # print(f'(after) DEBUG: {Neighbors=}')
            return

        Neighbors = {}
        for i in range(len(Favorites)):
            Neighbors.setdefault(i, set())
        twoChains = set()
        for employee, favorite in enumerate(Favorites):
            Neighbors[favorite].add(employee)
            if Favorites[favorite] == employee:
                pair = tuple(sorted((employee, favorite)))
                twoChains.add(pair)
        # print(f'{Neighbors=}')
        print(f'{twoChains=}')

        twoChainAnswer = 0
        for pair in twoChains:
            print(f'Check 2-chain {pair}:')
            chainLengths = []
            for employee in pair:
                # print(f'  for {employee}:')
                chainLengths.append(
                    maxChainLength(employee, pair)
                )
            # print(f'  ... {chainLengths=}')
            chainLengths.sort(reverse=True)
            chainLengths = chainLengths[:2]
            print(f'  twoChainAnswer += 2 + sum({chainLengths})')
            twoChainAnswer += 2 + sum(chainLengths)
            # include all such groups

        deleteLeafChains()

        for pair in twoChains:
            for employee in pair:
                Neighbors[employee].pop()
        # print(f'(deleted) DEBUG: {Neighbors=}')

        if len(outdegreeNonZero) <= 5:
            print(f'{outdegreeNonZero=}')
        else:
            print(f'{len(outdegreeNonZero)=}')
        cycleAnswer = 0
        while outdegreeNonZero:
            test = outdegreeNonZero.pop()
            if test in outdegreeZero:
                assert test not in outdegreeZero
                continue
            cycleLen = 1 + maxChainLength(test, (test,))
            print(f'  {test=}: {cycleLen=}')
            cycleAnswer = max(cycleAnswer, cycleLen)
            if len(Neighbors[test]):
                Neighbors[test].pop()
                neighborCount[test] -= 1
                assert neighborCount[test] >= 0
                if neighborCount[test] == 0:
                    outdegreeZero.add(test)
                    if test in outdegreeNonZero:
                        outdegreeNonZero.remove(test)
            deleteLeafChains()

        return max(twoChainAnswer, cycleAnswer)

# NOTE: Acceptance Rate 38.1% (HARD)

# NOTE: Time Limit Exceeded

