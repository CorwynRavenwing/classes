class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        partial_subsets = [[]]
        print(f'--- PS={len(partial_subsets)}')
        print(f'--- {partial_subsets=}')
        for N in nums:
            new_partials = [
                PS + [N]
                for PS in partial_subsets
            ]
            print(f'{N=} {new_partials=}')
            partial_subsets.extend(new_partials)
            print(f'{N=} PS={len(partial_subsets)}')
        return partial_subsets

