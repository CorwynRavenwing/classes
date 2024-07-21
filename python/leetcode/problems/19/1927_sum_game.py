class Solution:
    def sumGame(self, num: str) -> bool:

        def scores(s: str) -> Tuple[int,int]:
            (Q, Score) = (0, 0)
            for C in s:
                if C == '?':
                    Q += 1
                else:
                    Score += int(C)
            return (Q, Score)
        
        halfway = len(num) // 2
        lefthalf = num[:halfway]
        righthalf = num[halfway:]
        print(f'{halfway=} {lefthalf=} {righthalf=}')

        (leftQ, leftScore) = scores(lefthalf)
        (rightQ, rightScore) = scores(righthalf)
        print(f'{leftQ=} {leftScore=} {rightQ=} {rightScore=}')
        
        if (leftQ + rightQ) % 2 == 1:
            print(f'Odd number of moves: Alice moves last, and wins')
            return True
        else:
            print(f'Even number of moves: Bob has a chance ...')

        if (leftQ == 0) and (rightQ == 0):
            print(f'  No moves!')
            if leftScore == rightScore:
                print(f'    Currently balanced: Bob wins')
                return False
            else:
                print(f'    Currently unbalanced: Alice wins')
                return True
        
        if leftQ == rightQ:
            print(f'  Equal turns on each side')
            if leftScore == rightScore:
                print(f'    Currently balanced: Bob matches Alice and wins')
                return False
            else:
                print(f'    Currently unbalanced: Alice can always choose to make it worse')
                return True
        else:
            print(f'  Different turns on each side.')
        
        if leftQ and rightQ:
            print(f'    Some "?" on each side.  Bob matches Alice and it doesnt get worse')
            print(f'      This continues until either [leftQ] or [rightQ] is zero,')
            print(f'      and all "?" are on the same side.')
        
        matchTurns = min(leftQ, rightQ)
        leftQ -= matchTurns
        rightQ -= matchTurns
        print(f'    new {leftQ=} {leftScore=} {rightQ=} {rightScore=}')
        # without loss of generality, let's say "left" is the side with no remaining moves
        if leftQ:
            (leftQ, rightQ) = (rightQ, leftQ)
            (leftScore, rightScore) = (rightScore, leftScore)
            print(f'    swap {leftQ=} {leftScore=} {rightQ=} {rightScore=}')
        
        difference = leftScore - rightScore
        if difference < 0:
            print(f'  Right score is already too high: nothing Bob can do')
            return True
        
        diff_mod_9 = difference % 9
        print(f'  {difference=} %={diff_mod_9}')
        if diff_mod_9 != 0:
            print(f'    Difference is not divisible by 9: Bob cant force a win')
            return True
        
        print(f'  {difference//9=} {rightQ//2=}')
        if (difference // 9) == (rightQ // 2):
            print(f'    Bob can force a win by complementing Alices moves: 0,9 1,8 2,7 3,6 4,5')
            return False
        else:
            print(f'    Bob cannot force a win by complementing Alices moves.  Poor Bob.')
            return True
# NOTE: Runtime 88 ms Beats 95.04%
# NOTE: Memory 17.81 MB Beats 17.36%
