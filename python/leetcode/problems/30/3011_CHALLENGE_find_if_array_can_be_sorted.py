class Solution:
    def canSortArray(self, nums: List[int]) -> bool:

        def setBits(N: int) -> int:
            # make binary string: "1100"
            # turn string to list of integers: [1, 1, 0, 0]
            # add list: 2
            return sum(
                map(
                    int,
                    f'{N:b}'
                )
            )
        groups = []
        current_group = []
        current_bits = -1
        for N in nums:
            B = setBits(N)
            print(f'GG={len(groups)} G={current_group} {N=} b={N:b} {B=}')
            if current_bits != B:
                if current_group:
                    print(f'  File {current_group=} under {current_bits=}')
                    groups.append(current_group)
                current_group = []
                current_bits = B
            current_group.append(N)
        print(f'  File {current_group=} under {current_bits=}')
        groups.append(current_group)
        current_group = []
        current_bits = B
        
        print(f'{groups}')
        for G1, G2 in pairwise(groups):
            print(f'{G1=}')
            print(f'{G2=}')
            if max(G1) > min(G2):
                print(f'  NO.  {max(G1)=} > {min(G2)=}')
                return False
            else:
                print(f'  ok')

        return True

# NOTE: Accepted on first Submit
# NOTE: Runtime 182 ms Beats 11.40%
# NOTE: Memory 16.80 MB Beats 16.58%
# NOTE: re-ran for challenge and recieved:
# NOTE: Runtime 111 ms Beats 5.45%
# NOTE: Memory 16.89 MB Beats 23.35%
# NOTE: ... slightly slower, vastly worse percentage
# NOTE: ... slightly more memory, much better percentage
