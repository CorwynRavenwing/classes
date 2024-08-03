class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        adjacent = {}
        for (A, B) in edges:
            adjacent.setdefault(A, set())
            adjacent.setdefault(B, set())
            adjacent[A].add(B)
            adjacent[B].add(A)
        # print(f'{adjacent=}')
        
        groups = {}
        seen = set()
        for i in adjacent.keys():
            # print(f'{i=}')
            if i in seen:
                # print(f'  (seen)')
                continue
            else:
                seen.add(i)
            groups.setdefault(i, set())
            queue = {i}
            while queue:
                Q = queue.pop()
                # print(f'  {Q=}')
                groups[i].add(Q)
                for A in adjacent[Q]:
                    if A not in seen:
                        seen.add(A)
                        # print(f'    +{A}')
                        queue.add(A)
                    # else:
                    #     print(f'    {A} seen')
            # print(f'{groups[i]=}')
        print(f'{len(groups)=}')
        ungrouped = n - len(adjacent)
        print(f'{ungrouped=}')

        twiceAnswer = [
            # each node in this group is disconnected from each node NOT in this group
            len(groupMembers) * (n - len(groupMembers))
            for groupID, groupMembers in groups.items()
        ] + [
            # each node NOT in a group is disconnected from all other nodes full stop
            ungrouped * (n - 1)
        ]
        print(f'{twiceAnswer=}')

        return sum(twiceAnswer) // 2    # we've counted each disconnect from both ends
# NOTE: Runtime 1711 ms Beats 22.88%
# NOTE: Memory 77.78 MB Beats 68.98%
