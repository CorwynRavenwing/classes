class Solution:
    def longestMountain(self, arr: List[int]) -> int:

        answer = 0
        beginMountain = None
        state = 'fall'
        for i, N in enumerate(arr):
            print(f'[{i}] {N} {state}')
            if i == 0:
                print(f'  start')
                continue
            P = arr[i-1]
            if P > N:
                if state == 'fall':
                    continue
                elif state == 'rise':
                    print(f'  mountain peak [{i-1}]')
                    state = 'fall'
                else:
                    print(f'  Unknown {state=}')
                    return -88888
            elif P < N:
                if state == 'rise':
                    continue
                elif state == 'fall':
                    print(f'  end mountain [{i - 1}]')
                    state = 'rise'
                    if beginMountain is not None:
                        size = i - beginMountain
                        print(f'    mountain {size=}')
                        answer = max(answer, size)
                    beginMountain = i - 1
                    print(f'  begin mountain [{i - 1}]')
                else:
                    print(f'  Unknown {state=}')
                    return -88888
            else:
                assert P == N
                if state == 'fall':
                    print(f'  end mountain [{i - 1}]')
                    if beginMountain is not None:
                        size = i - beginMountain
                        print(f'    mountain {size=}')
                        answer = max(answer, size)
                print(f'  flat section [{i-1},{i}]')
                beginMountain = None
                state = 'fall'
        if state == 'fall':
            if beginMountain is not None:
                size = len(arr) - beginMountain
                print(f'End mountain {size=}')
                answer = max(answer, size)
            else:
                print(f'No mountains')
        else:
            print(f'No incomplete mountain')

        return answer

