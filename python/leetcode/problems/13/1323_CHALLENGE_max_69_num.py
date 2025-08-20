class Solution:
    def maximum69Number (self, num: int) -> int:
        
        # Note 1: the number will *decrease* if you change
        #   a 9 to a 6, so that will never help

        # Note 2: the number will increase *most* if you
        # change the *leftmost* 6 to a 9.

        nStr = list(str(num))
        print(f'{nStr=}')

        if '6' not in nStr:
            print(f"No sixes: changes won't help")
            return num
        
        index = nStr.index('6')
        print(f'Replace 6 at {index=}')
        nStr[index] = '9'

        answer = int(''.join(nStr))

        return answer

# NOTE: Acceptance Rate 82.0% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.84 MB Beats 28.83%
