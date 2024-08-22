class Solution:
    def findComplement(self, num: int) -> int:

        binary = f'{num:b}'
        print(f'{binary=}')

        complement = ''.join([
            str(1 - int(D))
            for D in binary
        ])
        print(f'{complement=}')
        
        answer = int(complement, 2)
        return answer

# NOTE: Accepted on first Run; Accepted on first Submit
# NOTE: Runtime 38 ms Beats 30.88%
# NOTE: Memory 16.39 MB Beats 89.59%
