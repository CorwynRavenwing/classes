class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

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
        
        answer = ""
        work = s
        while work:
            print(f'"{answer}" <- "{show(work)}"')
            letters = sorted(list(set(work)))
            for L in letters:
                index = work.index(L)
                print(f'  "{L}": [{index}]')
                left = work[:index]
                center = work[index]
                right = work[index+1:]
                assert center == L
                print(f'    "{show(left)}" "{center}" "{show(right)}"')
                missing = set(left) - set(right)
                if missing:
                    missingStr = "".join(sorted(list(missing)))
                    print(f'      missing="{missingStr}"')
                    continue
                else:
                    answer += L
                    workList = filter_away_EQ(right, L)
                    work = ''.join(workList)
                    # print(f'      -> "{show(work)}"')
                    break

        return answer

        while to_work:
            L = len(to_work)
            work = to_work.pop()
            print(f'{L=} cache={len(cache)} W={len(work)}')
            # print(f'  "{show(work)}"')
            if work in cache:
                print(f'    cache hit')
                continue
            else:
                # print(f'    cache miss')
                (first, rest) = (work[:1], work[1:])
                if first in rest:
                    rest_clean = ''.join(
                        filter_away_EQ(rest, first)
                    )
                else:
                    rest_clean = rest
                keep_this = (first, rest_clean)
                cache[work] = ([],[keep_this])
                to_work.append(rest_clean)
                # print(f'    +{first},{show(rest_clean)}')
                if first in rest:
                    skip_this = ("", rest)
                    cache[work][1].append(skip_this)
                    to_work.append(rest)
                    # print(f'    -{show(rest)}')

        # print(f'{type("")=}')   # <class 'str'>
        # print(f'{type([])=}')   # <class 'list'>
        # print(f'{type({})=}')   # <class 'dict'>

        return "xyzzy"



        wrap = 1000
        min_show = 2
        skip_first = True

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

