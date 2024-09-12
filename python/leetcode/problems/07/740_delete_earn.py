class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        # we borrow some code from #3186:

        nums.sort()
        print(f'{len(nums)=}')
        counts = Counter(nums)
        nums_pairs = sorted(counts.items())
        nums_N = [N for (N, count) in nums_pairs]
        nums_count = [count for (N, count) in nums_pairs]
        print(f'{len(nums_N)    =}')
        print(f'{len(nums_count)=}')

        # @cache    # must roll our own ignoring 'depth' parameter
        DP_cache = [None] * (len(nums_N) + 1)
        def DP(orig_index: int, depth=0) -> int:

            index = orig_index
            
            margin = '  ' * depth

            answer = DP_cache[orig_index]
            if answer is not None:
                return answer

            if index >= len(nums_N):
                answer = 0
                DP_cache[orig_index] = answer
                return answer

            print(f'{margin}DP({orig_index})')
            take = 0
            N = nums_N[index]
            try:
                # if you take one N, take them all
                print(f'{margin}  take {N} * {nums_count[index]} [{index}]')
                take += N * nums_count[index]
                while nums_N[index] == N:
                    # SHOULD only happen once
                    index += 1
                while nums_N[index] <= N + 1:
                    print(f'{margin}  -no- {nums_N[index]} [{index}]')
                    index += 1
            except IndexError:
                pass
            take += DP(index, depth+1)
            print(f'{margin}  {take=}')

            index = orig_index
            
            try:
                # if you skip one N, skip them all
                print(f'{margin}  skip {N} [{index}]')
                while nums_N[index] == N:
                    # SHOULD only happen once
                    index += 1
            except IndexError:
                pass
            skip = DP(index, depth+1)
            print(f'{margin}  {skip=}')

            print(f'{margin}  answer: {take=} {skip=}')
            answer = max(take, skip)
            DP_cache[orig_index] = answer
            return answer
        
        print(f'prime cache in reverse, from {len(nums_N)} to {0}')
        for i in reversed(range(len(nums_N))):
            print(f'{i=} prime cache')
            ignore = DP(i)

        return DP(0)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 130 ms Beats 5.11%
# NOTE: Memory 19.40 MB Beats 26.96%
