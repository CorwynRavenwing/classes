class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        wrap = 1000
        min_show = 2
        skip_first = True

        def show(s: str) -> str:
            t = f'{s[:10]}...{s[-10:]}({len(s)})'
            return (
                t
                if len(t) < len(s)
                else s
            )
        
        def filter_away_EQ(group: List[str], target: str) -> List[str]:
            if target not in group:
                return group
            return [
                G
                for G in group
                if G != target
            ]

        def filter_away_GT(group: List[str], target: str) -> List[str]:
            return [
                G
                for G in group
                if G <= target
            ]
        
        possibles = [
            ("", s)
        ]
        print(f'L=0 ("", "", "{show(s)}")')
        answer = None
        P = None
        while P or possibles:
            L = len(possibles)
            if P is None:
                possibles.sort()
                P = possibles.pop(0)
            (past, remain) = P
            (current, future) = (remain[:1], remain[1:])
            if L % wrap == 0 or len(past) >= min_show:
                print(f'{L=} ("{show(past)}", "{current}", "{show(future)}")')
            if (answer is not None) and (past > answer):
                print(f'    prune {show(past)}')
                P = None
                continue
            if not remain:
                print(f'    FOUND "{past}"')
                answer = (
                    min(answer, past)
                    if answer is not None
                    else past
                )
                P = None
                possibles = filter_away_GT(possibles, (answer,))
                new_L = len(possibles)
                if new_L != L:
                    print(f'    PRUNE {L - new_L}')
                    L = new_L
                continue
            # print(f'    "{past}" "{current}" "{future}"')

            if current in future:
                future_trim = ''.join(
                    filter_away_EQ(future, current)
                )
            else:
                future_trim = future
            copy_current = (past + current, future_trim)
            skip_current = (past, future)
            # try copying the current letter:
            P = None
            if current not in past:
                # print(f'      {copy_current=}')
                if copy_current not in possibles:
                    if not skip_first:
                        P = copy_current    # do it immediately instead
                    else:
                        possibles.append(copy_current)
                # else:
                #     print(f'      (dup copy)')
            # else:
            #     print(f'      cant copy current: already in past')
            # try skipping the current letter:
            if current in future or current in past:
                # print(f'      {skip_current=}')
                if skip_current not in possibles:
                    if skip_first:
                        P = skip_current    # do it immediately instead
                    else:
                        possibles.append(skip_current)
                # else:
                #     print(f'      (dup skip)')
            # else:
            #     print(f'      cant skip current: not in future or past')
        print(f'{answer=}')
        return answer

# NOTE: in progress, still times out on large inputs
