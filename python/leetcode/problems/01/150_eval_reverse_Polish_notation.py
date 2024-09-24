class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operators = ['+', '-', '*', '/']
        OPER = {
            '+': lambda A, B: (A + B),
            '-': lambda A, B: (A - B),
            '*': lambda A, B: (A * B),
            '/': lambda A, B: int(A / B),   # round towards zero.  A//B would round toward -INF.
        }
        stack = []
        for T in tokens:
            if T not in operators:
                print(f'push {T=}')
                stack.append(int(T))
            else:
                B = stack.pop()
                print(f'  pop {B=}')
                A = stack.pop()
                print(f'  pop {A=}')
                C = OPER[T](A, B)
                stack.append(C)
                print(f'push {C} = {A} {T} {B}')
        D = stack.pop()
        print(f'\npop {D=}')
        return D

# NOTE: Accepted on first Submit
# NOTE: Runtime 79 ms Beats 8.24%
# NOTE: Memory 17.17 MB Beats 12.32%
