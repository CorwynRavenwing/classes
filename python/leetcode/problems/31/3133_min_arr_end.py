class Solution:
    def minEnd(self, n: int, x: int) -> int:
        
        REVSTR = lambda x: ''.join(reversed(x))

        def bin_rev(N: int) -> str:
            binary = f'{N:b}'
            answer = REVSTR(binary)
            # print(f'bin_rev({N}) {binary=} {answer=}')
            return answer
        
        def int_rev(S_rev: str) -> int:
            S = REVSTR(S_rev)
            answer = int(S, 2)
            # print(f'int_rev({S_rev}) {S=} {answer=}')
            return answer

        x_bin_rev = bin_rev(x)  # only do this work once

        def merge_unset_bits(i: int) -> int:
            # print(f'merge_unset_bits({i}):')
            i_bin_rev = bin_rev(i)
            # print(f'  {i_bin_rev=}')
            x_clean = x_bin_rev.replace('0', '_')
            # print(f'  {x_clean=}')
            if i_bin_rev != '0':
                for D in i_bin_rev:
                    if '_' not in x_clean:
                        x_clean += '_'
                        # print(f'  {x_clean=}')
                    x_clean = x_clean.replace('_', D, 1)
                    # print(f'  {x_clean=}')
            # else:
            #     # print(f'  Merge 0 == keep current value')
            
            x_clean = x_clean.replace('_', '0')
            answer = int_rev(x_clean)
            # print(f'  {answer=}')

            return answer

        # for i in range(n):
        #     # print(f'{n=} {i=} {x=} {merge_unset_bits(i)=}')

        return merge_unset_bits(n - 1)

# NOTE: Runtime 40 ms Beats 36.98%
# NOTE: Memory 16.62 MB Beats 5.73%
