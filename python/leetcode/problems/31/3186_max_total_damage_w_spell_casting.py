class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:

        # we borrow some code from #3180:
        # ... and it times out.
        # we borrow code from #3181 instead:
        # ... and it times out.
        # let's try a completely different approach.

        power.sort()    # but don't make it unique using set() this time
        print(f'{len(power)=}')
        counts = Counter(power)
        power_pairs = sorted(counts.items())
        power_N = [N for (N, count) in power_pairs]
        power_count = [count for (N, count) in power_pairs]
        print(f'{len(power_N)    =}')
        print(f'{len(power_count)=}')

        # @cache    # must roll our own ignoring 'depth' parameter
        DP_cache = [None] * (len(power_N) + 1)
        def DP(orig_index: int, depth=0) -> int:

            index = orig_index
            
            margin = '  ' * depth

            answer = DP_cache[orig_index]
            if answer is not None:
                return answer

            if index >= len(power_N):
                answer = 0
                DP_cache[orig_index] = answer
                return answer

            # print(f'{margin}DP({orig_index})')
            take = 0
            N = power_N[index]
            try:
                # if you take one N, take them all
                # print(f'{margin}  take {N} * {power_count[index]} [{index}]')
                take += N * power_count[index]
                while power_N[index] == N:
                    # SHOULD only happen once
                    index += 1
                while power_N[index] <= N + 2:
                    # print(f'{margin}  -no- {power_N[index]} [{index}]')
                    index += 1
            except IndexError:
                pass
            take += DP(index, depth+1)
            # print(f'{margin}  {take=}')

            index = orig_index
            
            try:
                # if you skip one N, skip them all
                # print(f'{margin}  skip {N} [{index}]')
                while power_N[index] == N:
                    # SHOULD only happen once
                    index += 1
            except IndexError:
                pass
            skip = DP(index, depth+1)
            # print(f'{margin}  {skip=}')

            # print(f'{margin}  answer: {take=} {skip=}')
            answer = max(take, skip)
            DP_cache[orig_index] = answer
            return answer
        
        print(f'prime cache in reverse, from {len(power_N)} to {0}')
        for i in reversed(range(len(power_N))):
            # print(f'{i=} prime cache')
            ignore = DP(i)

        return DP(0)

# NOTE: Finally successful (version 4)
# NOTE: Runtime 1587 ms Beats 34.05%
# NOTE: Memory 101.52 MB Beats 24.75%
