class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        # we borrow some code from #78:

        partial_subsets = {()}  # the set containing an empty tuple
        print(f'--- PS={len(partial_subsets)}')
        print(f'--- {partial_subsets=}')
        for N in nums:
            new_partials = {
                tuple(sorted(PS + (N,)))
                for PS in partial_subsets
            }
            print(f'{N=} {new_partials=}')
            partial_subsets |= new_partials
            print(f'{N=} PS={len(partial_subsets)}')
        return sorted(partial_subsets)

# NOTE: Runtime 44 ms Beats 25.84%
# NOTE: Memory 16.69 MB Beats 79.02%
