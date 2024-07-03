class Solution:
    def minDifference(self, nums: List[int]) -> int:

        # SHORTCUT 1: moving value X to the same location
        # that another value Y already is, is equivalent to
        # removing value X.  So we will do that instead.
        
        # SHORTCUT 2: on each move, only two things make
        # logical sense: moving the lowest current value, or
        # moving the highest.  Also, we only have 3 moves.
        # that means there are 2 ^ 3 == 8 possible actions.
        # Actually, some of them are duplicates:
        # Low Low High == High Low Low for example.
        # So actually there are only (LLL LLH LHH HHH) == 4
        # possibilities total.
        # THEREFORE we use brute force without apology.

        # SHORTCUT 3: if we have 4 numbers, we can use our
        # three moves to move three of them to be the fourth
        # and get a span of zero.  With fewer numbers, this
        # is even easier.
        # The case [A B C D D D D D] is equivalent but harder
        # to detect, so I'm going to avoid shorcutting that.
        
        if len(nums) <= 4:
            return 0
        
        def span(nums: List[int]) -> int:
            return (
                max(nums) - min(nums)
                if nums
                else 0
            )

        def show_span(label: str, nums: List[int]) -> None:
            # print(f'{label}: {span(nums)} ({nums})')
            print(f'{label}: {span(nums)}')
            return
        
        def MoveL(nums: List[int]) -> List[int]:
            answer = nums.copy()
            answer.remove(min(answer))
            return answer
        
        def MoveR(nums: List[int]) -> List[int]:
            answer = nums.copy()
            answer.remove(max(answer))
            return answer

        show_span('begin', nums)
        L = MoveL(nums)
        R = MoveR(nums)
        show_span('L', L)
        show_span('R', R)

        LL = MoveL(L)
        LR = MoveR(L)
        RR = MoveR(R)
        show_span('LL', LL)
        show_span('LR', LR)
        show_span('RR', RR)

        LLL = MoveL(LL)
        LLR = MoveR(LL)
        LRR = MoveR(LR)
        RRR = MoveR(RR)
        show_span('LLL', LLL)
        show_span('LLR', LLR)
        show_span('LRR', LRR)
        show_span('RRR', RRR)

        possible = [LLL, LLR, LRR, RRR]
        # print(f'{possible=}')
        spans = list(map(span, possible))
        print(f'{spans=}')
        return min(spans)

