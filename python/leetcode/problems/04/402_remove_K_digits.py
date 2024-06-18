class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        print(f'{k=} {num=}')
        stack = []
        for digit in num:
            while k and stack and stack[-1] > digit:
                print(f'{k}: drop {stack[-1]} > {digit}')
                del stack[-1]
                k -= 1
            stack.append(digit)
        if k:
            print(f'{k=} {stack=}')
        while k and stack:
            print(f'{k}: drop {stack[-1]}: last')
            del stack[-1]
            k -= 1
        print(f'{k=} {stack=}')

        assert k == 0
        
        while stack and len(stack) > 1 and stack[0] == '0':
            print(f'0: drop leading zero')
            del stack[0]
        if stack == []:
            print(f'0: "" -> "0"')
            stack.append('0')
        
        return ''.join(stack)

