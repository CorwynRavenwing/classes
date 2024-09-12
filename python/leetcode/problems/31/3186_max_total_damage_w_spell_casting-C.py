class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:

        # we borrow some code from #3180:
        # ... and it times out.
        # we borrow code from #3181 instead:
        # ... and it times out.
        # let's try a completely different approach.

        power.sort()    # but don't make it unique using set() this time
        print(f'{len(power)=}')

        # @cache    # must roll our own ignoring 'depth' parameter
        DP_cache = [None] * (len(power) + 1)
        def DP(orig_index: int, depth=0) -> int:

            index = orig_index
            
            margin = '  ' * depth

            answer = DP_cache[orig_index]
            if answer is not None:
                return answer

            if index >= len(power):
                answer = 0
                DP_cache[orig_index] = answer
                return answer

            # print(f'{margin}DP({orig_index})')
            take = 0
            N = power[index]
            try:
                while power[index] == N:
                    # if you take one N, take them all
                    # print(f'{margin}  take {N} [{index}]')
                    take += N
                    index += 1
                while power[index] <= N + 2:
                    # print(f'{margin}  -no- {power[index]} [{index}]')
                    index += 1
            except IndexError:
                pass
            take += DP(index, depth+1)
            # print(f'{margin}  {take=}')

            index = orig_index
            
            try:
                while power[index] == N:
                    # if you skip one N, skip them all
                    # print(f'{margin}  skip {N} [{index}]')
                    index += 1
            except IndexError:
                pass
            skip = DP(index, depth+1)
            # print(f'{margin}  {skip=}')

            # print(f'{margin}  answer: {take=} {skip=}')
            answer = max(take, skip)
            DP_cache[orig_index] = answer
            return answer
        
        print(f'prime cache in reverse, from {len(power)} to {0}')
        for i in reversed(range(len(power))):
            # print(f'{i=} prime cache')
            ignore = DP(i)

        return DP(0)

# NOTE: Timeout for large inputs
