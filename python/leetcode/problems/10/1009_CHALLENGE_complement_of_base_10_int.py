class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        binary = f'{n:b}'
        print(f'{binary=}')

        complement = ''.join([
            str(1 - int(D))
            for D in binary
        ])
        print(f'{complement=}')
        
        answer = int(complement, 2)
        return answer

# NOTE: Accepted on first Submit
# NOTE: Runtime 42 ms Beats 7.01%
# NOTE: Memory 16.46 MB Beats 56.35%

# NOTE: Acceptance Rate 60.6% (easy)

# NOTE: re-ran for challenge:
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 19.26 MB Beats 86.82%
# NOTE: infinitely faster, infinitely better percentage
# NOTE: slightly more memory, but much better percent
