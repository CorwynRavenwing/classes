class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        # PROCESS:
        # we sort each item into place in two flips:
        # 1) flip with K= location of maximum unsorted item
        # 2) flip with K= location this item goes to (e.g. last)

        # SHORTCUT:
        # since our output is identical in either case, we will
        # delete already-sorted items from the end of the list.
        # that means our process is now:
        # 0) delete any sorted items at end of list
        # 1) flip k=index of max
        # 2) flip k=current length
        
        answer = []

        REV = lambda x: list(reversed(list(x)))

        def flip(k: int):
            nonlocal arr
            nonlocal answer
            if k == 1:
                print(f'  Flip({k}): SKIP')
                return
            answer.append(k)
            arr[:k] = REV(arr[:k])
            print(f'  Flip({k})')
            return

        pattern = sorted(arr)
        while arr:
            print(f'A={arr}')
            # print(f'P={pattern}')
            while arr and pattern and arr[-1] == pattern[-1]:
                del arr[-1]
                del pattern[-1]
                print(f'D={arr}')
            if not arr:
                continue
            Max = pattern[-1]
            Index = arr.index(Max)
            flip(Index + 1)
            print(f'M={arr}')
            flip(len(arr))
        
        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 15 ms Beats 96.14%
# NOTE: Memory 16.82 MB Beats 18.49%
