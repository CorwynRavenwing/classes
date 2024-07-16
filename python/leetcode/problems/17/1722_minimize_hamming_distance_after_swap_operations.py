class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:

        def hamming(S: List[int], T: List[int]) -> int:
            return sum([
                (
                    0
                    if Snum == Tnum
                    else 1
                )
                for (Snum, Tnum) in zip(S, T)
            ])
        
        def swapGroups(swaps: List[List[int]]) -> List[List[int]]:
            
            parent = {}
            def topLevel(N: int) -> int:
                # print(f'TL({N}):')
                nonlocal parent
                if N not in parent:
                    parent[N] = N
                    # print(f'  A:{N}')
                    return N
                P = parent[N]
                if P == N:
                    # print(f'  B:{P}')
                    return N
                P = topLevel(P)
                parent[N] = P
                # print(f'  C:{P}')
                return P

            def merge(M: int, N: int) -> None:
                # print(f'merge({M},{N}):')
                nonlocal parent
                M = topLevel(M)
                N = topLevel(N)
                if M == N:
                    # print(f'  already')
                    return
                parent[M] = N
                # print(f'  joined')
                return

            for (A, B) in swaps:
                merge(A, B)
            groups = {}
            # print(f'Setup groups:')
            for C in parent.keys():
                P = topLevel(C)
                groups.setdefault(P, [])
                groups[P].append(C)
                # print(f'  {C} in group {P}')
            # print(f'{groups=}')

            return list(groups.values())

        def pickIndexes(indexes: List[int], sourceList: List[int]) -> List[int]:
            return [
                sourceList[I]
                for I in indexes
            ]

        def changeHammingWithSwapGroup(swapGroup: List[int]) -> int:
            nonlocal source, target
            S = pickIndexes(swapGroup, source)
            T = pickIndexes(swapGroup, target)
            local_hd_before = hamming(S, T)
            # instead of composing a new S and remeasuring Hamming,
            # we throw out any elements that match and count the remainder.
            S_count = Counter(S)
            T_count = Counter(T)
            S_set = set(S_count)
            T_set = set(T_count)
            local_hd_after = 0
            for s_item, s_count in S_count.items():
                t_count = T_count[s_item]
                if s_count > t_count:
                    local_hd_after += s_count - t_count
                    # print(f'{s_item}: {s_count} > {t_count}')
            hd_change = local_hd_after - local_hd_before
            # print(f'hamming distance changed by {local_hd_after}-{local_hd_before} = {hd_change}')
            return hd_change

        hd = hamming(source, target)
        # print(f'{hd=}')

        sg = swapGroups(allowedSwaps)
        # print(f'{sg=}')

        print(f'Original Hamming = {hd}')
        for S in sg:
            print(f'  swap Group {S[:5]}...')
            change = changeHammingWithSwapGroup(S)
            print(f'  -> {change=}')
            hd += change

        return hd
# NOTE: 933 ms; Beats 86.52%
