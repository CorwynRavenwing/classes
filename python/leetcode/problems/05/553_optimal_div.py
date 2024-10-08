class Solution:
    def optimalDivision(self, nums: List[int]) -> str:

        DEBUG = False

        def doDivision(nums: List[int]) -> float:
            if DEBUG: print(f'DD({nums}):')
            if len(nums) == 1:
                answer = nums[0]
            else:
                answer = doDivision(nums[0]) / doDivision(nums[1])
            if DEBUG: print(f'DD({nums}): {answer}')
            return answer
        
        def doFormat(nums: List[int], needParens=False) -> str:
            if len(nums) == 1:
                answer = f'{nums[0]}'
            else:
                (A, B) = nums
                Astr = doFormat(A)
                Bstr = doFormat(B, True)
                answer = f'{Astr}/{Bstr}'
                if needParens:
                    answer = f'({answer})'
            return answer

        def ultimateDivision(nums: List[int], wantMax: bool) -> str:
            if DEBUG: print(f'UD({nums},{wantMax}):')
            if len(nums) == 1:
                answer = nums
            else:
                answers = []
                for i in range(1, len(nums)):
                    A = nums[:i]
                    B = nums[i:]
                    if DEBUG: print(f'UD({nums},{wantMax}): {A=} {B=}')
                    Adiv = ultimateDivision(A, wantMax)
                    Bdiv = ultimateDivision(B, not wantMax)
                    if DEBUG: print(f'UD({nums},{wantMax}): {Adiv=} {Bdiv=}')
                    Cdiv = (Adiv, Bdiv)
                    answers.append(
                        (
                            doDivision(Cdiv),
                            Cdiv,
                        )
                    )
                # print(f'DEBUG: about to sort answers:')
                # for A in answers:
                #     if DEBUG: print(f'  DEBUG {A=}')
                answers.sort(key=lambda x: x[0])    # field #0 is the quotient
                chosen = (
                    answers[-1]
                    if wantMax else
                    answers[0]
                )
                if DEBUG: print(f'UD({nums},{wantMax}): {chosen=}')
                (quotient, answer) = chosen
            if DEBUG: print(f'UD({nums},{wantMax}): {answer=}')
            return answer
        
        return doFormat(
            ultimateDivision(tuple(nums), True)
        )

# NOTE: Runtime 203 ms Beats 5.15%
# NOTE: Memory 16.88 MB Beats 9.70%
