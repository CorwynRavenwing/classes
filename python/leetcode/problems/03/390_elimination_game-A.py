class Solution:
    def lastRemaining(self, n: int) -> int:

        def filter_numbers(group: List[int], deleteFirst: bool) -> List[int]:
            if len(group) == 1:
                return group
            matchMod = (
                1
                if deleteFirst
                else 0
            )
            return list([
                G
                for i, G in enumerate(group)
                if i % 2 == matchMod
            ])

        debug = True
        # group = list(range(1, n+1))
        group = [
            (N, format(N, '04b'))
            for N in list(range(1, n+1))
        ]

        passes = 0
        if debug:
            print(f'{group[0]} ... {group[-1]}:')
        if debug:
            print(f'^^:^ {group[:4]}...{group[-1]} len={len(group)}')
        while len(group) > 1:
            # left to right:
            group = filter_numbers(group, True)
            passes += 1
            if debug:
                print(f'RX:{passes} {group[:4]}...{group[-1]} len={len(group)}')
            if len(group) > 1:
                # right to left:
                is_odd = len(group) % 2 != 0
                group = filter_numbers(group, is_odd)
                passes += 1
                if debug:
                    print(f'L{"A" if is_odd else "B"}:{passes} {group[:4]}...{group[-1]} len={len(group)}')
            else:
                if debug:
                    print(f'L:{passes} SKIP')
        return group[0][0]

# NOTE: this is a naive design, and runs out of memory for large cases.
