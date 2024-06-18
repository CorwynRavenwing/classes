class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        
        # we reuse some code from problem #78

        partial_subsets = [[]]
        # print(f'--- PS={len(partial_subsets)}')
        # print(f'--- {partial_subsets=}')
        for N in nums:
            new_partials = [
                PS + [N]
                for PS in partial_subsets
                if (
                    ((N + k) not in PS)
                ) and (
                    ((N - k) not in PS)
                )
            ]
            # print(f'{N=} {new_partials=}')
            partial_subsets.extend(new_partials)
            # print(f'{N=} PS={len(partial_subsets)}')
        # print(f'{partial_subsets=}')
        return len(partial_subsets) - 1
        # -1 because PS includes the (invalid by rules) empty subset

