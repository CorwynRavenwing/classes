class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        possibles = [
            ("", s)
        ]
        answer = None
        while possibles:
            print(f'L={len(possibles)}')
            possibles.sort()
            P = possibles.pop(0)
            print(f'  {P=}')
            (past, remain) = P
            if (answer is not None) and (past > answer):
                print(f'    prune')
                continue
            if not remain:
                print(f'    FOUND "{past}"')
                answer = (
                    min(answer, past)
                    if answer is not None
                    else past
                )
                continue
            (current, future) = (remain[0], remain[1:])
            # print(f'    "{past}" "{current}" "{future}"')
            if current in future:
                future_trim = ''.join([
                    F
                    for F in future
                    if F != current
                ])
            else:
                future_trim = future
            copy_current = (past + current, future_trim)
            skip_current = (past, future)
            # try copying the current letter:
            if current not in past:
                # print(f'      {copy_current=}')
                if copy_current not in possibles:
                    possibles.append(copy_current)
                # else:
                #     print(f'      (dup copy)')
            # else:
            #     print(f'      cant copy current: already in past')
            # try skipping the current letter:
            if current in future or current in past:
                # print(f'      {skip_current=}')
                if skip_current not in possibles:
                    possibles.append(skip_current)
                # else:
                #     print(f'      (dup skip)')
            # else:
            #     print(f'      cant skip current: not in future or past')
        print(f'{answer=}')
        return answer

# NOTE: in progress

