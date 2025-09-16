class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:

        DEBUG = False

        stack = []
        A = None
        B = None
        while nums or A is not None or B is not None:
            if DEBUG: print(f'[{len(stack)}] {A},{B}:')
            if B is None:
                if len(nums):
                    B = nums.pop(0)
                    continue
                else:
                    break
            if A is None:
                A = B
                B = None
                continue
            if A is None or B is None:
                raise Exception(f'{A=} or {B=} is {None}')
            if gcd(A, B) == 1:
                if DEBUG: print(f'  coprime: push stack')
                stack.append(A)
                A = None
                continue
            else:
                if DEBUG: print(f'  non-coprime: replace')
                B = lcm(A, B)
                A = None
                if len(stack):
                    if DEBUG: print(f'     pop stack')
                    A = stack.pop(-1)
                continue
        if A is not None:
            if DEBUG: print(f'[{len(stack)}] {A},{B}: push A')
            stack.append(A)
            A = None
        if B is not None:
            if DEBUG: print(f'[{len(stack)}] {A},{B}: push B')
            stack.append(B)
            B = None
        if DEBUG: print(f'[{len(stack)}] {A},{B}: done')
        return stack

# NOTE: Acceptance Rate 42.0% (HARD)

# NOTE: Accepted on second Run (fencepost error)
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 6296 ms Beats 5.43%
# NOTE: Memory 28.50 MB Beats 97.83%
