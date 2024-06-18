class Solution:
    def canTransform(self, start: str, end: str) -> bool:

        def LR_indexes(string: str) -> dict[str,List[int]]:
            answers = {
                'L': [],
                'R': [],
                'X': [],
            }
            for i, S in enumerate(string):
                answers[S].append(i)
            return answers
        
        S = LR_indexes(start)
        E = LR_indexes(end)
        for letter in 'LRX':
            if len(S[letter]) != len(E[letter]):
                print(f'  Nope, different number of "{letter}"')
                return False
        for (A, B) in zip(S['L'], E['L']):
            if A < B:
                print(f'  Nope, letter L needs to move right ({A},{B})')
                return False
        for (A, B) in zip(S['R'], E['R']):
            if A > B:
                print(f'  Nope, letter R needs to move left ({A},{B})')
                return False

        while start and end:
            printing = (len(start) < 20)
            if printing:
                print(f'S="{start}"')
                print(f'E="{end}"')
            # else:
            #     print(f'S={len(start)} E={len(end)}')

            if start == end:
                print(f'  SUCCESS!')
                return True

            working = False
            while start[0] == end[0]:
                if printing:
                    print(f'  pop start {start[0]}')
                start = start[1:]
                end = end[1:]
                working = True
            while start[-1] == end[-1]:
                if printing:
                    print(f'  pop end {start[-1]}')
                start = start[:-1]
                end = end[:-1]
                working = True
            if working:
                continue

            S = LR_indexes(start)
            E = LR_indexes(end)
            if printing:
                print(f'{S=}')
                print(f'{E=}')
            working = False
            for (A, B) in zip(S['L'], E['L']):
                if A < B:
                    print(f'  Nope, letter L needs to move right ({A},{B})')
                    return False
                elif A > B:
                    if printing:
                        print(f'  L {A}->{B}')
                    # check letters leftwards from A .. B
                    # if they are all Xs, swap past all of them
                    # stop at beginning of string or first non-X
                    xindex = A - 1
                    while xindex >= 0 and xindex >= B and start[xindex] == 'X':
                        # print(f'{xindex=} {0} {B} "{start[xindex]}"')
                        xindex -= 1
                    # we subtracted one too many
                    xindex += 1
                    buncha_Xs = start[xindex:A]
                    assert buncha_Xs == "X" * len(buncha_Xs)
                    if len(buncha_Xs) == 0:
                        if printing:
                            print(f'cant move L: "{start[A-1]}"')
                    else:
                        old_len = len(start)
                        start = (
                            start[:xindex] + start[A] + buncha_Xs + start[A+1:]
                            # before the Xs  the "L"    the Xs      after the "L"
                        )
                        new_len = len(start)
                        assert old_len == new_len
                        working = True
            for (A, B) in zip(S['R'], E['R']):
                if A > B:
                    print(f'  Nope, letter R needs to move left ({A},{B})')
                    return False
                elif A < B:
                    if printing:
                        print(f'  R {A}->{B}')
                    # check letters rightwards from A .. B
                    # if they are all Xs, swap past all of them
                    # stop at end of string or first non-X
                    xindex = A + 1
                    while xindex < len(start) and xindex <= B and start[xindex] == 'X':
                        # print(f'{xindex=} {len(start)} {B} "{start[xindex]}"')
                        xindex += 1
                    # we added one too many
                    xindex -= 1
                    buncha_Xs = start[A+1:xindex+1]
                    assert buncha_Xs == "X" * len(buncha_Xs)
                    if len(buncha_Xs) == 0:
                        if printing:
                            print(f'cant move R: "{start[A+1]}"')
                    else:
                        old_len = len(start)
                        start = (
                            start[:A] + buncha_Xs + start[A] + start[xindex+1:]
                            # before R  the Xs      the "R"    after the Xs
                        )
                        new_len = len(start)
                        assert old_len == new_len
                        working = True
            if working:
                continue
            else:
                print(f'FAIL')
                return False

        return True

