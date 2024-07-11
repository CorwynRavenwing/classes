class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        prereqs = {
            # course: {set, of, prereq, courses}
        }
        for (P, C) in prerequisites:
            prereqs.setdefault(C, set())
            prereqs[C].add(P)

        prereqCache = {}

        def getAllPrereqs(C: int, depth=0) -> Set[int]:
            nonlocal prereqs, prereqCache
            if C in prereqCache:
                # print(f'{margin}getAllPrereqs({C}): cache hit')
                return prereqCache[C]
            margin = '  ' * depth
            if C not in prereqs:
                # print(f'{margin}getAllPrereqs({C}): none')
                prereqCache[C] = set()
                return set()
            # print(f'{margin}getAllPrereqs({C}): {prereqs[C]}')
            prereqSet = prereqs[C].copy()
            for CK in prereqs[C]:
                # only do this once: getAllPrereqs returns deep answers
                PS = getAllPrereqs(CK, depth + 1)
                # if PS:
                #     print(f'    -> {PS}')
                prereqSet |= PS
            # print(f'{margin}gAP({C}) -> {prereqSet}')
            prereqCache[C] = prereqSet
            return prereqSet
        
        def checkPrereq(P: int, C: int) -> bool:
            return P in getAllPrereqs(C)
        
        return [
            checkPrereq(*Q)
            for (Q) in queries
        ]
# NOTE: 588 ms; Beats 53.09%
