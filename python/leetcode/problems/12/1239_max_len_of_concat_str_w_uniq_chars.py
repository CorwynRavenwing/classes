class Solution:
    def maxLength(self, arr: List[str]) -> int:

        def DP_dont(index: int, seen: List[str]) -> int:
            # try:
            #     word = arr[index]
            # except IndexError:
            #     return 0
            return DP(index + 1, seen)
        
        def DP_pick(index: int, seen: List[str]) -> int:
            # try:
            word = arr[index]
            # except IndexError:
            #     return 0
            counts = Counter(word)
            maxcounts = counts.most_common(1)
            (letter, maxcount) = maxcounts.pop()
            # print(f'{maxcount=}')
            if maxcount > 1:
                print(f'Cannot use "{word}": duplicate {letter=}')
                return 0
            
            seen_set = set(seen)
            use_now_set = set(counts.keys())
            # print(f'{use_now_set=}')

            intersection = use_now_set & seen_set
            if intersection:
                print(f'Cannot use "{word}": {seen=}')
                print(f'  -> {intersection=}')
                return 0
            
            new_seen_set = use_now_set | seen_set
            new_seen = tuple(sorted(new_seen_set))
            return len(word) + DP(index + 1, new_seen)

        @cache
        def DP(index: int, seen: List[str]) -> int:
            try:
                word = arr[index]
            except IndexError:
                return 0
            
            return max([
                DP_pick(index, seen),
                DP_dont(index, seen),
            ])
        
        return DP(0, ())

# NOTE: Accepted on first Submit
# NOTE: Without cache:
# NOTE: Runtime 299 ms Beats 22.15%
# NOTE: Memory 16.79 MB Beats 44.79%
# NOTE: With cache:
# NOTE: Runtime 311 ms Beats 22.15%
# NOTE: Memory 37.88 MB Beats 6.04%
# NOTE: Time actually SLOWER but same percentage; memory TWICE as high.
